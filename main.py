# import json module, for reading save files
import json
# import sys module, for command line
import sys
# import ast.literal_eval(), for testing and printing the output
from ast import literal_eval
# import Chip class
from Chip import Chip

# Definition:   function create_chip_file(Chip, string)
# Arguments:    Chip chip_obj, string file_name
# Purpose:      Saves Chip object into file with path
#               equal to file_name.
# Notes:        Find out how to set "creationIndex" value!!!
#               Also, currently no way to set colour - default is blue.
def create_chip_file(chip_obj, file_name):
    """
    returns nothing.
    
    parameters:
        chip_obj (Chip): chip that contains only and/not gates,
        file_name (str): the name of the file to be created
        
    extra:
        -currentley no way to choose the color of the chip
    """
    try:
        create_chip = open(file_name, "w")
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
                "componentNameList": (chip_obj.chipComponents),
                "savedComponentChips": (chip_obj.components)
            }, create_chip, indent = 4)
        except:
            print(f"Could not dump chip! Printable version: {repr(chip_obj)}")
            quit(1)
    except:
        print(f"Could not open output file! Requested file: {file_name}")
        quit(1)


# Definition:   function create_new_chip(Chip)
# Arguments:    Chip chip
# Purpose:      Recursive function, which resolves any
#               possible dependencies on chip
# Notes:        Second argument MUST BE LEFT TO DEFAULT!!!
#               It is used internally, as a saved version of
#               original chip argument
def create_new_chip(chip, return_chip=None):
    """
    returns a "Chip" object which contains only "and" and "not" gates
    
    arguments:
        chip (Chip): used for recursion stuff when calling this function you should pass in the chip you wish to compile,
        return_chip (Chip): this is ONLY used for recursion, do NOT set this to anything when calling this function
        
    Returns:
        a "Chip" object that contains only "and" and "not" gates
    """
    builtin_components = ["AND", "NOT", "SIGNAL IN", "SIGNAL OUT"]
    other_components = []

    # if its the first iteration of recursion then return chip = chip
    if return_chip == None:
        return_chip = chip

    # Check if the chip has other chips inside it
    for component in chip.chipComponents:
        if component not in builtin_components:
            # move component from chipComponents to other_components
            other_components.append(component)
            return_chip.chipComponents.remove(component)

    # possibly unnecessary?
    return_chip.chipComponents = builtin_components

    # if our chip is made of only and/not gates, return "return_chip" untouched
    if other_components == []:
        return return_chip

    # otherwise, recursively try to insert new chips

    # TODO: write code that appends new chip to old one.
    else:
        for component in range(len(chip.chipComponents)):
            if chip.chipComponents[component] in other_components:
                data = chip.chipComponents[component]
                componentInputs = data['inputPins']
                new_chip = create_new_chip(Chip(f"{chip.chipComponents[component]['name']}.txt"))
                for newComponent in new_chip['chipComponents']:
                    if newComponent['name'] in ['SIGNAL IN', 'SIGNAL OUT']:
                        del(newComponent)
        # for other_component in other_components:
        #     new_chip = Chip(f"{other_component}.txt")
        #     return_chip.componentData.append(repr(create_new_chip(new_chip, return_chip)))
        # return return_chip

# TESTING
chip_test = Chip("NAND.txt")
new_chip = create_new_chip(chip_test)
print(json.dumps(literal_eval(repr(new_chip)), sort_keys=True, indent=4))
