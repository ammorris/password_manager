import os.path

# load the json file
json_file_name = "passwords.json"

if os.path.exists(json_file_name):
	json_file = open(json_file_name, "r")
else:
	json_file = open(json_file_name, "w")

modes = ["load", "l", "save", "s"]

mode = "whatever"
while mode not in modes:
	mode = input("Do you want to load or save a password? ")

if mode == "load" or mode == "l":
	pass
elif mode == "save" or mode == "s":
	site = input("Enter site name: ")
	password = input("Enter password to save: ")

json_file.close()