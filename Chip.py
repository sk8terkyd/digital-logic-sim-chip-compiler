import json


class Chip:
    
    # Description: This class is used for dealing with chips in an easier
    # way.
    # Arguments: str file_path
    # Purpose: Retrieves and organizes the data for the Chip.
    # Notes: Fully rewritten

    def __init__(self, file_path):
        
        # Load data

        chipFile = open(file_path)
        self.chipRawData = json.load(chipFile)
        chipFile.close()

        # Sort data

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

        # Make formal data for Chip

        self.chipData = {'name': self.chipName, 'chipComponents': self.chipComponents, 'componentData': self.componentData}

    def __repr__(self):
        return str(self.chipData)