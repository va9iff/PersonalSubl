import sublime
import sublime_plugin
import threading
import subprocess
import os

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

