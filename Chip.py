import json

# Definition:   function read_file(string)
# Arguments:    string file_path
# Purpose:      Reads file specified by path given, returns
#               string with contents
# Notes:        Couldn't possibly be safer ;)
def read_file(file_path):
    """
    returns the content of the given file path
    
    args:
        "file_path"(string)
    """
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
    """
    returns a python dict of a given json string
    
    args:
        "json_string"(string)
    """
    try:
        return json.loads(json_string)
    except:
        print(f"Could not parse contents of file! Contents: {json_string}")
        quit(1)


# Definition:   class Chip(string)
# Arguments:    string file_path
# Purpose:      Packs all internals of chip into one neat object
# Notes:        It seems to be safe (catches all exceptions)
class Chip:
    """
    Chip class is used for "main.py"
    """
    def __init__(self, file_path):
        # initializing the values that matter to us
        self.path = file_path
        try:
            self.json_text = read_file(self.path)
        except:
            print(f"Needed chip file not found! Path to chip file: {file_path}")
            quit(1)
        self.dict_with_parts = read_json(self.json_text)
        # name of chip
        self.name = self.dict_with_parts["name"]
        # components that the chip is made of
        self.component_name_list = self.dict_with_parts["componentNameList"]
        # actual components section of chip
        self.components = self.dict_with_parts["savedComponentChips"]

    # returning the important values
    def __repr__(self):
        return repr(f"""name: {self.name},""" +
                    f"""component names: {self.component_name_list},""" +
                    f"""components: {self.components}""")
