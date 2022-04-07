import sublime
import sublime_plugin
import os
from ..myUtils import top_active_folder
# requires node and live-server installed I think
class LiveServerOnItsTopFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.status_message('Live Server at >> '+top_active_folder(self))
		os.system('start /min cmd /K live-server '+top_active_folder(self))
