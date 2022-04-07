print("Personaal:")
import sublime
import sublime_plugin
import os
import subprocess

from .myUtils import top_active_folder
from .Commandios.test import TestCommand
from .Commandios.cmd import OpenCmdTopFolderCommand,OpenCmdFileCommand
from .Commandios.live_server import LiveServerOnItsTopFolderCommand
from .Commandios.prettier import PrettierAsyncCommand
print("	imports are done")


# a cute example
# class PersonalOpenTopFolderCommand(sublime_plugin.WindowCommand):
	# def run(self):
		# os.system('explorer '+top_active_folder(self))


class MyTerminusCloseAll(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("terminus_close_all")
		self.window.status_message("Closed all Terminus instances on this window")

print("	we're all done")
