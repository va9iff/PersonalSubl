
def top_active_folder(window_command):
	folders = window_command.window.folders()
	active_file = window_command.window.active_view().file_name()

	# print(folders)
	# print(active_file)

	if active_file and folders:
		for folder in folders:
			# means string of name is in path of folder
			if folder in active_file:
				return folder

	elif not active_file and folders:
		return folders[0]


	elif active_file and not folders:
		return os.path.dirname(active_file)

