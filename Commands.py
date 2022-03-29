import sublime
import sublime_plugin
import os
import subprocess
# import json
import threading

from .myUtils import top_active_folder



class TestCommand(sublime_plugin.WindowCommand):
	def run(self):
		print('< TEST')
		# print(os.path.dirname(self.window.active_view().file_name()))
		print('TEST >')



class OpenCmdFileCommand(sublime_plugin.WindowCommand): # V
	def run(self):
		print('start cmd at', self.window.active_view().file_name())
		os.popen('start cmd /K cd '+os.path.dirname(self.window.active_view().file_name()))


class OpenCmdTopFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.status_message('CMD at >> '+top_active_folder(self))
		os.popen('start cmd /K cd '+top_active_folder(self))


# requires node and live-server installed I think
class LiveServerOnItsTopFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.status_message('Live Server at >> '+top_active_folder(self))
		os.system('start /min cmd /K live-server '+top_active_folder(self))



# a cute example
# class PersonalOpenTopFolderCommand(sublime_plugin.WindowCommand):
	# def run(self):
		# os.system('explorer '+top_active_folder(self))


class PrettierAsyncCommand(sublime_plugin.WindowCommand):
	def prettifyWithStatusMsg(self, win):
		cmd = 'prettier --write --use-tabs  --arrow-parens "avoid" --no-semi "'+win.active_view().file_name()+'"'

		sb = subprocess.Popen(cmd, shell=True, 
							stdout=subprocess.PIPE,
							stderr = subprocess.PIPE,
							# stdin = subprocess.PIPE
							)
		subprocess_return = sb.stdout.read() + sb.stderr.read() 
		output = subprocess_return.decode("utf-8") 
		output = output.replace("\\n","\n")

		panel = win.create_output_panel("Prettier")
		panel.settings().set("gutter", False)

		panel.set_read_only(False)
		panel.run_command("append", {"characters":output})
		panel.set_read_only(True)

		win.run_command('revert')

		if len(str(output).split("\n")) == 2:
			win.status_message(output)
			# win.run_command('hide_panel', {"panel":"output.Prettier"})
		else:
			win.run_command('show_panel', {"panel":"output.Prettier"})


	def run(self):
		thr = threading.Thread(target=self.prettifyWithStatusMsg, args=(self.window,), kwargs={})
		thr.start()


class MyTerminusCloseAll(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("terminus_close_all")
		self.window.status_message("Closed all Terminus instances on this window")
