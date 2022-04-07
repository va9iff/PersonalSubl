import sublime
import sublime_plugin
import os
from ..myUtils import top_active_folder

class OpenCmdFileCommand(sublime_plugin.WindowCommand): # V
	def run(self):
		print('start cmd at', self.window.active_view().file_name())
		os.popen('start cmd /K cd '+os.path.dirname(self.window.active_view().file_name()))


class OpenCmdTopFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.status_message('CMD at >> '+top_active_folder(self))
		os.popen('start cmd /K cd '+top_active_folder(self))

