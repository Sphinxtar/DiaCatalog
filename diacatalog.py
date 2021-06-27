#!/usr/bin/python3
import os
import sys

path = '/home/linus/.local/lib/python3.9/site-packages/diagrams'
mods = os.listdir(path)

def modlist():
	print("Systems available: ")
	mods = os.listdir(path)
	for f in mods:
		if not f.startswith("_"):
			print("\t",f)

def modlistsub(subsys):
	mpath = path+'/'+subsys
	print("\n--- "+subsys)
	mods = os.listdir(mpath)
	for f in mods:
		if not f.startswith("_"):
			print('\n------',f.rsplit(".",1)[0])
			m = str(mpath+'/'+f)
			claz = open(m)
			for clazline in claz:
				clazzes = clazline.split( )
				if len(clazzes) != 0:
					if clazzes[0] == "class":
						if not clazzes[1].startswith("_"):
							id = clazzes[1].split('(')
							if len(id) != 0:
								print("\t",id[0])
			claz.close()

def modlistall():
	mods = os.listdir(path)
	for f in mods:
		if not f.startswith("_"):
			print('\n----',f)
			modpath = str(path+'/'+f)
			modus = os.listdir(modpath)
			for m in modus:
				if not m.startswith("_"):
					print('\n\t',m.rsplit(".",1)[0])
					#print("\n\t",m.rstrip('.py'))
					claz = open(modpath+'/'+m)
					for clazline in claz:
						clazzes = clazline.split( )
						if len(clazzes) != 0:
							if clazzes[0] == "class":
								if not clazzes[1].startswith("_"):
									id = clazzes[1].split('(')
									if len(id) != 0:
										print("\t\t",id[0])
					claz.close()

if os.path.isdir(path) != True:
	print("No such path: ", path)
	print("Change the path line at top of this script to your home directory and stay the hell out of mine!")	
	quit()

if len(sys.argv) < 2:
	modlist()
elif sys.argv[1] == 'all':
	modlistall()
else:
	if os.path.isdir(path+'/'+sys.argv[1]) != True:
		print("No such sub system, use with no arguments for a list or 'all' for everything.")
	else:
		modlistsub(sys.argv[1])
quit()

