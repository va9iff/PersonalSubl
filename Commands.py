import sublime
import sublime_plugin
import os
import subprocess
import json
import threading


def top_active_folder(window_command):
	folders = window_command.window.folders()
	active_file = window_command.window.active_view().file_name()

	print(folders)
	print(active_file)

	if active_file and folders:
		for folder in folders:
			# means string of name is in path of folder
			if folder in active_file:
				return folder

	elif not active_file and folders:
		return folders[0]


	elif active_file and not folders:
		return os.path.dirname(active_file)





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
		print('start cmd at', top_active_folder(self))
		os.popen('start cmd /K cd '+top_active_folder(self))


# requires node and live-server installed I think
class LiveServerOnItsTopFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		print('Live Server at',top_active_folder(self))
		os.system('start /min cmd /K live-server '+top_active_folder(self))



# a cute example
# class PersonalOpenTopFolderCommand(sublime_plugin.WindowCommand):
	# def run(self):
		# os.system('explorer '+top_active_folder(self))

# reqs: node and prettier installed
# Build doesn't block the app, so I'll use prettier with build
# but issue: building changes the last build (the one that's on ctrl b)
class PrettierDontSaveCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cmd_command = "prettier --use-tabs --arrow-parens \"avoid\" --no-semi"
		cmd_command +=  ' "'+self.view.file_name()+'"'
		output = os.popen(cmd_command).read()
		output_string = output.replace('\\n','\n')
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, output_string)


# requres node and prettier installed
# class BuildPrettierHideOutputCommand(sublime_plugin.WindowCommand):
# 	def run(self):
# 		self.window.run_command("save", {"async": False})
# 		self.window.run_command("build", {"build_system": "Packages/Personal/External Tools/Node Tools/Prettier/Prettier - code format.sublime-build", "choice_build_system": True, "choice_variant": True, "variant": ""})
# 		self.window.run_command("hide_panel", {"panel": "output.exec"})



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




class ZetupPersonalPreferencesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		prefs_path = os.path.join(sublime.packages_path(), 'User', 'Preferences.sublime-settings')
		personal_prefs_path = os.path.join(sublime.packages_path(), 'Personal', 'Personal Settings', 'Preferences.sublime-settings')
		prefs           = open(prefs_path,'w')
		personal_prefs  = open(personal_prefs_path)
		prefs.write(personal_prefs.read())

		prefs.close()
		personal_prefs.close()

class ZetupPersonalKeybindingCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		prefs_path = os.path.join(sublime.packages_path(), 'User', 'Default (Windows).sublime-keymap')
		personal_prefs_path = os.path.join(sublime.packages_path(), 'Personal', 'Personal Settings', 'Default (Windows).sublime-keymap')
		prefs           = open(prefs_path,'w')
		personal_prefs  = open(personal_prefs_path)
		prefs.write(personal_prefs.read())

		prefs.close()
		personal_prefs.close()

class ZetupInputHandler(sublime_plugin.ListInputHandler):
	def list_items(self):
		return [
		("key bindings", "keys"),
		("preferences", "prefs"),
		]

class ZetupPersonalCommand(sublime_plugin.WindowCommand):
	def run(self, zetup = "prefs"):
		if zetup == "keys":
			self.window.run_command("zetup_personal_keybinding")
		elif zetup == "prefs":
			self.window.run_command("zetup_personal_preferences")
	def input(self, args):
		return ZetupInputHandler()




class UpdatePersonalPreferencesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		prefs_path = os.path.join(sublime.packages_path(), 'User', 'Preferences.sublime-settings')
		personal_prefs_path = os.path.join(sublime.packages_path(), 'Personal', 'Personal Settings', 'Preferences.sublime-settings')
		prefs           = open(prefs_path)
		personal_prefs  = open(personal_prefs_path, 'w')
		personal_prefs.write(prefs.read())

		prefs.close()
		personal_prefs.close()

class UpdatePersonalKeybindingCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		prefs_path = os.path.join(sublime.packages_path(), 'User', 'Default (Windows).sublime-keymap')
		personal_prefs_path = os.path.join(sublime.packages_path(), 'Personal', 'Personal Settings', 'Default (Windows).sublime-keymap')
		prefs           = open(prefs_path)
		personal_prefs  = open(personal_prefs_path, 'w')
		personal_prefs.write(prefs.read())

		prefs.close()
		personal_prefs.close()

class UpdateInputHandler(sublime_plugin.ListInputHandler):
	def list_items(self):
		return [
		("key bindings", "keys"),
		("preferences", "prefs"),
		]

class UpdatePersonalCommand(sublime_plugin.WindowCommand):
	def run(self, update = "prefs"):
		if update == "keys":
			self.window.run_command("update_personal_keybinding")
		elif update == "prefs":
			self.window.run_command("update_personal_preferences")
	def input(self,args):
		return UpdateInputHandler()

