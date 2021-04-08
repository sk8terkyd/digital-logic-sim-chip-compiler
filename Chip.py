import json
import os

class Chip:
    
    # Description: This class is used for dealing with chips in an easier
    # way.
    # Arguments: str file_path
    # Purpose: Retrieves and organizes the data for the Chip.
    # Notes: Fully rewritten

    def __init__(self, file_path):
        
        # Load data

        try:
            chipFile = open(file_path)
            self.chipRawData = json.load(chipFile)
            chipFile.close()
        except:
            print("Your file was not found. Please ensure that it is in the same directory as this project, and that you are running this code in the parent directory of this project.")
            quit()
        # Sort data
        
        try:
            self.chipName = self.chipRawData['name']
            self.chipComponents = self.chipRawData['componentNameList']

            # Only keep the important things

            self.componentData = []

            for chipUsed in range(len(self.chipRawData['savedComponentChips'])):

                # Get data of all chips used

                chipUsedData = {'name': self.chipRawData['savedComponentChips'][chipUsed]['chipName'], 'inputPins': self.chipRawData['savedComponentChips'][chipUsed]['inputPins'], 'outputPinNames': self.chipRawData['savedComponentChips'][chipUsed]['outputPinNames']}
                
                # Add data of the chips that are not built in NOT IMPLEMENTED
                
                # if not chipUsedData['name'] in ['SIGNAL IN', 'SIGNAL OUT', 'AND', 'NOT']:
                #     chipUsedData['componentData'] = repr(Chip(f"{chipUsedData['name']}.txt"))

                # Add data to components for this Chip

                self.componentData.append(chipUsedData)
        
        except:
            print("Are you sure this is a Chip save file, in json form? Please check your save file, just in case.")
            quit()

        # Make formal data for Chip

        self.chipData = {'name': self.chipName, 'chipComponents': self.chipComponents, 'componentData': self.componentData}

    def __repr__(self):
        return str(self.chipData)
        