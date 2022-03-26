import sublime
import sublime_plugin
import os
# import json


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

