################################################################################
############################ Chip Class ########################################
################################################################################


import json

# Definition:   function read_file(string)
# Arguments:    string file_path
# Purpose:      Reads file specified by path given, returns
#               string with contents
# Notes:        Couldn't possibly be safer ;)
def read_file(file_path):
    try:
        file = open(file_path, 'r')
        try:
            return file.read()
        except:
            print(f"Could not read file! Path to requested file: {file_path}")
            quit(1)
        finally:
            file.close()
    except:
        print(f"Requested file not found! Path to requested file: {file_path}")
        quit(1)


# Definition:   function read_json(string)
# Arguments:    string json_string
# Purpose:      Takes in contents of file written in JSON,
#               turns it into Python's dictionary type
# Notes:        Error handling added
def read_json(json_string):
    try:
        return json.loads(json_string)
    except:
        print(f"Could not parse contents of file! Contents: {json_string}")
        quit(1)
