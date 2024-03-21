import sys

raw_dir_file = sys.argv[1]
with open(raw_dir_file + "/test_build.py", "r") as file:
	filedata = file.read()

arduino_cli_path = sys.argv[2]
filedata = filedata.replace("arduino-cli", arduino_cli_path)

with open(raw_dir_file + "/test_build_modified.py", "w") as file:
	file.write(filedata)
