import json

def create_chip_file(chip_obj, file_name, mode="x"):
    """
    Purpose: it creates a chip file with the name being passed in by user
    Arguments: chip_obj (Chip), file_name (str), mode (can be "w" or "x")
    Example: If i pass in NAND as chip_obj, "NAND_COMPILED" as file_name,
    and "w" as mode, it will open the file called "NAND_COMPILED", and if it exists,
    it will write the the json_string of "chip_obj" into the file.
    Notes: cannot choose the color of chip. Haven't tested the changes i have made
    yet.
    """
    try:
        create_chip = open(file_name, mode)
        try:
            json.dump({
                "name": (chip_obj.name),
                "creationIndex": 0,
                "colour": {
                    "r": 0.0,
                    "g": 0.0,
                    "b": 1.0,
                    "a": 1.0
                },
                "nameColour": {
                    "r": 1.0,
                    "g": 1.0,
                    "b": 1.0,
                    "a": 1.0
                },
                "componentNameList": (chip_obj.component_name_list),
                "savedComponentChips": (chip_obj.components)
            }, create_chip, indent = 4)
        except:
            print(f"Could not dump chip! Printable version: {repr(chip_obj)}")
            quit(1)
    except:
        print(f"Could not open output file! Requested file: {file_name}")
        quit(1)
