# import json module, for reading save files
import json
# import sys module, for command line
import sys
# import ast.literal_eval(), for testing and printing the output
from ast import literal_eval
# import os, for file existence checking
import os
# import Chip class
from Chip import Chip

# Definition:   function create_chip_file(Chip, string)
# Arguments:    Chip chip_obj, string file_name
# Purpose:      Saves Chip object into file with path
#               equal to file_name.
# Notes:        Find out how to set "creationIndex" value!!!
#               Also, currently no way to set colour - default is blue.
def create_chip_file(chip_obj):
    """
    returns nothing.
    
    parameters:
        chip_obj (Chip): chip that contains only and/not gates,
        file_name (str): the name of the file to be created
    """
    
    file_name = input("What is the name of the file you wish that your chip save will be exported to? (Please do not use an existing file, as it will not work properly.)    ")

    if os.path.exists(file_name):
        print("Please use a filepath that does not exist to export your chip save to.")
        quit()

    print(
            """
            Instructions:
            If numbers are asked for, input them as numbers, not words.
            If it asks for a number, give a decimal number (e.g. 0-255 in the case of RGB), not a hexadecimal number (e.g. 00-FF) for RGB.
            """
        )

    try:
        create_chip = open(os.path.join("saveFiles", file_name), "w")
        try:
            json.dump({
                "name": (chip_obj.chipName),
                "creationIndex": 0,
                "colour": {
                    "r": float(input("The R part of the RGB:   "))/255,
                    "g": float(input("The G part of the RGB:   "))/255,
                    "b": float(input("The B part of the RGB:   "))/255,
                    "a": 1.0
                },
                "nameColour": {
                    "r": 1.0,
                    "g": 1.0,
                    "b": 1.0,
                    "a": 1.0
                },
                "componentNameList": chip_obj.chipData['chipComponents'],
                "savedComponentChips": chip_obj.chipData['componentData']
            }, create_chip, indent = 4)
        except:
            print(f"Could not dump chip! Printable version: {repr(chip_obj)}. This is most likely an internal error. Go to [NOT YET MERGED, ISSUES TAB WILL NOT EXIST] and submit a Issue in the Issues tab.") # If you do fork this, just put the link https://github.com/sk8terkyd/digital-logic-sim-chip-compiler/issues there.
            quit(1)
    except:
        print(f"Could not create/open output file! Requested file: {file_name}. Be sure to include the file extension.  This is most likely an internal error. Go to [NOT YET MERGED, ISSUES TAB WILL NOT EXIST] and submit a Issue in the Issues tab.") # If you do fork this, just put the link https://github.com/sk8terkyd/digital-logic-sim-chip-compiler/issues there.")
        quit(1)


# Definition:   function create_new_chip(Chip)
# Arguments:    Chip chip
# Purpose:      Recursive function, which resolves any
#               possible dependencies on chip
# Notes:        Second argument removed.
def create_new_chip(chip):
    """
    returns a "Chip" object which contains only "and" and "not" gates
    
    arguments:
        chip (Chip): used for recursion stuff when calling this function you should pass in the chip you wish to compile
        
    Returns:
        a "Chip" object that contains only "and" and "not" gates
    """
    builtin_components = ["AND", "NOT", "SIGNAL IN", "SIGNAL OUT"]
    other_components = []
    
    return_chip = chip

    # Check if the chip has other chips inside it

    for component in return_chip.chipComponents:
        if not(component in builtin_components):
            # move component from chipComponents to other_components
            other_components.append(component)
            return_chip.chipComponents.remove(component)

    # if our chip is made of only and/not gates, return "return_chip" untouched
    if other_components == []:
        return return_chip

    # otherwise, recursively try to insert new chips

    else:
        for component in range(len(return_chip.componentData)):
            if return_chip.componentData[component]['name'] in other_components:
                data = return_chip.componentData[component]
                componentInputs = data['inputPins']
                try:
                    new_chip = create_new_chip(Chip(os.path.join("saveFiles", f"{return_chip.componentData[component]['name']}.txt")))
                except:
                    try:
                        new_chip = create_new_chip(Chip(os.path.join("saveFiles", f"{return_chip.componentData[component]['name']}.json")))
                    except:
                        print("Be sure that you have all the chip saves in the saveFiles folder of the folder you are running this from.")
                        quit()
                for newComponent in new_chip.chipData['componentData']:
                    for inputPin in newComponent['inputPins']:
                        if new_chip.chipData['componentData'][inputPin['parentChipIndex']]['name'] == 'SIGNAL IN':
                            inputPin['parentChipOutputIndex'] = componentInputs[inputPin['parentChipIndex']]['parentChipOutputIndex']
                            inputPin['parentChipIndex'] = componentInputs[inputPin['parentChipIndex']]['parentChipIndex']
                        else:
                            for inputPin in newComponent['inputPins']:
                                    inputPin['parentChipIndex'] += len(return_chip.chipData['componentData'])
                firstOut = True
                for newComponentNum in range(len(new_chip.chipData['componentData'])):
                    newComponent = new_chip.chipData['componentData'][newComponentNum]
                    if newComponent['name'] == 'SIGNAL OUT':
                        if firstOut:
                            firstOutNum = newComponentNum
                    for component in return_chip.componentData:
                        for inputPin in component['inputPins']:
                            if inputPin['parentChipIndex'] == component and inputPin['parentChipOutputIndex'] == firstOutNum - newComponentNum:
                                inputPin['parentChipIndex'] = len(chip.componentData) + newComponentNum
                for newComponent in new_chip.chipData['componentData']:
                    if newComponent['name'] in ['SIGNAL IN', 'SIGNAL OUT']:
                        del(newComponent)
                for chip in new_chip.chipData['componentData']:
                    return_chip.chipData['componentData'].append(chip)
        for chip in return_chip.chipData['componentData']:
            print(chip)
            chip['posX'] = 0.0
            chip['posY'] = 0.0
        return return_chip

print("Please run this process in the folder that has this code. Otherwise, it may not function properly.")
originalChip = Chip(input("What is the name of the file you would like to simplify?    "))
baseChip = create_new_chip(originalChip)
create_chip_file(baseChip)
print("Your simplified chip save has been made.")