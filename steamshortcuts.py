# Program to backup Steam Shortcuts
# HKEY_CLASSES_ROOT\steam\Shell\Open\Command

# for filename in os.listdir("C:\\temp"):
#     print  filename

import sys, os, shutil, datetime, time, platform

# The file we need to make backups of
maxdirsize = 0
maxfilesday = 0
my_os = platform.system() + " " + platform.release()
my_shortcuts = 'shortcuts.vdf'
my_steam = "D:\game\s\steam\config\\"

# I don't really care what OS I'm on.  I just care where Steam shortcuts.vdf is.

settings_file = 'settings.conf'

def startup():
	"""What am I trying to accomplish here"""

def maintenance():
	"""Check the size of the directory and too many backups"""
	for filename in os.listdir(os.path.dirname(__file__)):
		print  filename

def find_date():
	"""Create the date and return it as a string for our file naming"""
	now = datetime.datetime.now()
	return time.strftime("%Y%m%d.")

def backup_shortcuts(shortcut_file):
	"""Create the backup with a dated name. Takes the original filename and path as an argument."""
	print "Backing up the file:",shortcut_file
	#shutil.copyfile(shortcut_file,  find_date() + 'shortcuts.vdf')
	try:
		shutil.copyfile(shortcut_file,  find_date() + 'shortcuts.vdf')
	except IOError, message:
		if str(message).find("Errno 2") == -1:
			print message
		else:
			print "Check your path, could not find:",shortcut_file

def restore_shortcuts(shortcut_file):
	"""Stop Steam if it is running, restore the selected shortcut"""

 

#print my_os
#print platform.uname()
#print sys.maxsize()

backup_shortcuts(my_steam + my_shortcuts)
