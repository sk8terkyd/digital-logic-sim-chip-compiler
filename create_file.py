#!/bin/python

import json
import os

def create_chip_file(chip_obj, file_name):
    """
    returns nothing.
    
    parameters:
        chip_obj (Chip): chip that contains only and/not gates,
        file_name (str): the name of the file to be created
    """
    
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
        create_chip = open(file_name, "w")
        try:
            json.dump({
                "name": (chip_obj.chipName),
                "creationIndex": 0,
                "colour": {
                    "r": float(input("The R part of the RGB:   "))+1/256,
                    "g": float(input("The G part of the RGB:   "))+1/256,
                    "b": float(input("The B part of the RGB:   "))+1/256,
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
