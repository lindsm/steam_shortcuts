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
my_steam = "D:\games\steam\config\\"

settings_file = 'settings.conf'

# Main Program
# Copy the file, make backups, don't let things exceed a certain size or a certain filecount
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
	shutil.copyfile(shortcut_file,  find_date() + 'shortcuts.vdf')
 

print my_os

#backup_shortcuts(my_steam + my_shortcuts)
