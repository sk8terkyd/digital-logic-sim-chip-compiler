#!/bin/python

from get_others import get_others
from Chip import Chip

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
    
    return_chip = chip

    # Check if the chip has other chips inside it

    other_components = get_others(return_chip)

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
                    new_chip = create_new_chip(Chip(f"{return_chip.componentData[component]['name']}.txt"))
                except:
                    try:
                        new_chip = create_new_chip(Chip(f"{return_chip.componentData[component]['name']}.json"))
                    except:
                        print("Be sure that you have all the chip saves in the folder you are running this from.")
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
            chip['posX'] = 0.0
            chip['posY'] = 0.0
        return return_chip
        