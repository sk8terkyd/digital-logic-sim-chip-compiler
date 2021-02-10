################################################################################
################################## Description #################################
################################################################################
This tool takes chip ".txt" files for the game "digital logic sim" and turns them into chips that only contain "and" and "not" gates so that you can share them with other people easier

################################################################################
####################### Use Tutorial ###########################################
################################################################################
This tool is still incomplete, but is capable of producing results.
# INFO
To use the tool, go to main.py, enter the file path, and then, assuming you also have all the other chip's data in this directory, you should receive a python dictionary, which contains the information about the chip in only AND & NOT gates, along with the inputs and outputs, and how the gates are connected.
reference.json is a json file that explains the structure of the chip save files.
# TODO
- [x] add recursiveness into the program.
- [x] clean up the current output.
- [x] find a way of finding out how the system is hooked up.
- [] make a way of communicating how the system is hooked up?
- [] make that into ascii.
- [x] find a way to figure out what 'isCyclic' means. Never mind that was in reference.json
# How does the json file explain how the chips are hooked up?
The inputPins store each pin in a dictionary. The names of the pins in the "name" index. ParentChipIndex says that this input is the (parentChipIdex + 1)th chip in the json file, and parentChipOutputIndex says the input is from the (parentChipOutputIdex + 1)th output of that chip. OutputPinNames is prety self-explanatory. However, something to note about the SIGNAL IN and SIGNAL OUT pins is that they still have the outputPinNames/inputPins as empty lists. You won't need to worry about "posX" and "posY", as those describe the location of the chip during the chip construction process. "chipName" describes the name of the chip, so this should help track the chips that are in builtin_chips.