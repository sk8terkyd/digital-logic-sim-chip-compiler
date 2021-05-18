# import sys module, for command line
import sys
# import Chip class
from Chip import Chip
# import create_chip_file
from create_file import create_chip_file
# import get_others
from get_others import get_others
# import create_chip
from create_chip import create_new_chip

if len(sys.argv) < 3:
    print("Please provide two arguments.")

try:
    originalChip = Chip(sys.argv[1])
    baseChip = create_new_chip(originalChip)
    create_chip_file(baseChip, sys.argv[2])
except:
    print("Please provide valid paths for both arguments.")
    quit()

print("Your simplified chip save has been made.")
