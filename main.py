################################################################################
################################## READ ME #####################################
################################################################################
"""
If at any point you are looking at this code and you DONT know what it does OR
you have a question about it, Tell Me so i can explain better what it does. also
if you change anything put a comment that you changed it please
"""

# import json module, for reading save files
import json
# import sys module, for command line
import sys
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
                "componentNameList": (chip_obj.component_name_list),
                "savedComponentChips": (chip_obj.components)
            }, create_chip, indent = 4)
        except:
            print(f"Could not dump chip! Printable version: {repr(chip_obj)}")
            quit(1)
    except:
        print(f"Could not open output file! Requested file: {file_name}")
        quit(1)


# Definition:   class outputChip
# Arguments:    return_chip_data, string file_name
# Purpose:      Object that represents the chip.
# Notes:        Find a way to make the output look nicer.


class outputChip:
    def __init__(self, return_chip_data):
        self.data = return_chip_data
        self.chipNewData = []
        self.chipsUsed = []
        self.chipLinks = []
        for chip in return_chip_data['chipData']:
            self.chipsUsed.append(chip['chipName'])
            try:
                self.chipLinks.append(chip['inputData'])
            except:
                try:
                    self.chipLinks.append(chip['outputData'])
                except:
                    self.chipLinks.append(None)
            if not chip['chipName'] in builtin_components:
                self.chipNewData.append(chip['chipData'])
            else:
                self.chipNewData.append(None)
    def getReprData(self):
        self.reprScriptItems = [f"The name of this chip is {self.data['name']}. "]
        chipCounter = 0
        for chip in self.chipsUsed:
            self.reprScriptItems.append(f'This chip is a {chip} chip. It\'s inputs are {self.chipLinks[chipCounter]}. ')
            chipCounter += 1
        for chip in self.chipNewData:
            noneNew = True
            if chip != None:
                if noneNew:
                    self.reprScriptItems.append("\nThese are chips used in the main chip that are not built-in:")
                    noneNew = False
                self.reprScriptItems.append(f"\n{str(chip[0])}")
        self.reprScript = ''.join(self.reprScriptItems)

    def __repr__(self):
        self.getReprData()
        return self.reprScript

# Definition:   function create_new_chip(Chip)
# Arguments:    Chip chip
# Purpose:      Recursive function, which resolves any
#               possible dependencies on chip
# Notes:        Second argument MUST BE LEFT TO DEFAULT!!!
#               It is used internally, as a saved version of
#               original chip argument
#               Partial credit to: @bill090
def create_new_chip(chip, return_chip = None):
    """
    returns a "Chip" object which contains only "and" and "not" gates
    
    arguments:
        chip (Chip): used for recursion stuff when calling this function you should pass in the chip you wish to compile,
        return_chip (Chip): this is ONLY used for recursion, do NOT set this to anything when calling this function
        
    Returns:
        a "Chip" object that contains only "and" and "not" gates
    """
    other_components = []

    # make return_chip return all bulitin components and use recursiveness to get the rest. 
    return_chip = {'name': f'{chip.name}', 'usedParts' : chip.component_name_list, 'chipData': []}


    # Check if the chip has other chips inside it
    for component in chip.component_name_list:
        if component not in builtin_components:
            # move component from component_name_list to other_components
            other_components.append(component)
            return_chip.component_name_list.remove(component)

    # if our chip is made of only and/not gates, return "return_chip" untouched

    # otherwise, recursively try to insert new chips

    # Alternate code to get non-built-in chip info

    # for component in other_components:
    #     try:
    #         other_chip_components.append(create_new_chip(Chip(f"{component}.txt")), return_chip)
    #     except:
    #         try:
    #             other_chip_components.append(create_new_chip(Chip(f"{component}.json")), return_chip)
    #         except:
    #             other_chip_components.append(f"Could not find {component} input file. Tried both .json and .txt extensions.")
    
    for component in chip.components:
        inputPinData = []
        for inputPin in component['inputPins']:
            inputPinData.append({"pinName": inputPin['name'], "linkRelativeToSave": (inputPin['parentChipIndex'], inputPin['parentChipOutputIndex'])})
        if component['chipName'] == "SIGNAL IN":
            return_chip['chipData'].append({'chipName': component['chipName'], 'inputName': component['outputPinNames'][0]})
        elif component['chipName'] == "SIGNAL OUT":
            return_chip['chipData'].append({'chipName': component['chipName'], 'outputData': inputPinData})
        elif not component['chipName'] in builtin_components:
            return_chip['chipData'].append({'chipName': component['chipName'], 'inputData': inputPinData, 'chipData': [create_new_chip(Chip(f"{component['chipName']}.txt"))]})
        else:
            return_chip['chipData'].append({'chipName': component['chipName'], 'inputData': inputPinData})
    return outputChip(return_chip)

# TESTING

builtin_components = ["AND", "NOT", "SIGNAL IN", "SIGNAL OUT"]
chipFilePath = input("Please enter the path of your chip save file.  ")
chip_test = Chip(f"{chipFilePath}")
new_chip = create_new_chip(chip_test)
print(repr(new_chip))
