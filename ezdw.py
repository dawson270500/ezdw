import os
import sys
import urllib.request
import stat
##EzDw written by Bailey Dawson | Version 1
if sys.argv == 1:
	print("No File Provided, Exitting")
	sys.exit()
try:
	f = open(sys.argv[1], "r")
	name = ""
	version = ""
	license = ""
	mainFileName = ""
	mainFile = ""
	files = []
	filesName = []
	for ln in f:
		if "Name" in ln:
			name = ln.strip("Name-").strip("\n")
			continue
		if "Version" in ln:
			version = ln.strip("Version-").strip("\n")
			continue
		if "License" in ln:
			license = ln.strip("License-").strip("\n")
			continue
		if "-main" in ln:
			tempArr = ln.split(" ")
			mainFileName = tempArr[2]
			mainFile = tempArr[0].replace(" ", "").strip("\n")
			continue
		if "-f" in ln:
			tempArr = ln.split(" ")
			filesName.append(tempArr[2])
			files.append(tempArr[0].strip("-f").strip().strip("\n"))
			continue
	print("Do you want to install the following app?\nName: "+name+"\nVersion: "+version+"\nLicense: "+license+"")
	while True:
		men = input("Y/n =>")
		if men.lower() == "y":
			break
		elif men.lower() == "n":
			sys.exit()
		print("Invalid Input")

	if not os.path.isdir("/usr/src/ezdw/"):
		print("/usr/src/ezdw/ was missing, creating")
		os.mkdir("/usr/src/ezdw/")

	print("Downloading "+mainFileName)
	request = urllib.request.urlopen(mainFile)
	data = request.read()
	text = data.decode('utf-8')
	f = open("/bin/"+mainFileName.replace("\n", ""), "w")
	f.write(text)
	f.close()
	print("Downloaded "+mainFileName)

	os.chmod("/bin/"+mainFileName.replace("\n", ""), stat.S_IRWXO)
	#os.chmod("/bin/"+mainFileName.replace("\n", ""), stat.S_IXOTH)
	print("Permissions set for "+mainFileName)

	i = 0
	while i < len(files):
		print("Downloading "+filesName[i])
		request = urllib.request.urlopen(files[i])
		data = request.read()
		text = data.decode('utf-8')
		f = open("/usr/src/ezdw/"+name.replace("\n", "")+"/"+filesName[i], "w")
		f.write(text)
		f.close()
		print("Downloaded "+filesName[i])
		i = i+1


except FileNotFoundError:
	print("Invalid File Provided")