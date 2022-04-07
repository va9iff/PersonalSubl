import sublime
import sublime_plugin


class TestCommand(sublime_plugin.WindowCommand):
	def run(self):
		print('< TEST')
		# print(os.path.dirname(self.window.active_view().file_name()))
		print('TEST >')

