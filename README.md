################################################################################
################################## Description #################################
################################################################################
This tool takes chip ".txt" files for the game "digital logic sim" and turns them into chips that only contain "and" and "not" gates so that you can share them with other people easier

################################################################################
####################### Use Tutorial ###########################################
################################################################################
Currently this tool is INCOMPLETE and doesn't work yet so, there is no use tutorial yet

# TODO
- [x] add recursiveness into the program.
- [] clean up the current output.
- [x] find a way of finding out how the system is hooked up.
- [] make a way of communicating how the system is hooked up?
- [] make that into ascii.
- [] find a way to figure out what 'isCyclic' means.
# How does the json file explain how the chips are hooked up?
The inputPins store each pin in a dictionary. The names of the pins in the "name" index. ParentChipIndex says that this input is the (parentChipIdex + 1)th chip in the json file, and parentChipOutputIndex says the input is from the (parentChipOutputIdex + 1)th output of that chip. OutputPinNames is prety self-explanatory. However, something to note about the SIGNAL IN and SIGNAL OUT pins is that they still have the outputPinNames/inputPins as empty lists. You won't need to worry about "posX" and "posY", as those describe the location of the chip during the chip construction process. "chipName" describes the name of the chip, so this should help track the chips that are in builtin_chips.