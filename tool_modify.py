import sys
import os

raw_dir_file = sys.argv[1]
with open(raw_dir_file + "/test_build.py", "r") as file:
	filedata = file.read()

arduino_cli_path = sys.argv[2]
filedata = filedata.replace("arduino-cli", arduino_cli_path)

output_path = sys.argv[3]
replace_str = "compile\", \"--output-dir\", \"{0}".format(output_path)
filedata = filedata.replace("compile", replace_str)

with open(raw_dir_file + "/test_build_modified.py", "w") as file:
	file.write(filedata)
