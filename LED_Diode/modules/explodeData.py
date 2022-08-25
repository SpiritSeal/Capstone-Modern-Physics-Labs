# Explode the overall excel spreadsheet data in ./inputs/_Data_Try_2.xlsx into individual csv files for each color
sourceFile = 'inputs/_Data_Try_2.xlsx'
destinationFolder = 'inputs/'

# Columns are [Color, V_diode, V_battery]
'''
Example of a row in the spreadsheet:
['white', '0.0', '0.0']
'''
def explode_data(sourceFile, destinationFolder):
    import pandas as pd
    df = pd.read_excel(sourceFile)
    for i in df['Color']:
        df[df['Color'] == i].to_csv(destinationFolder + i + '.csv', index=False)
        print('Created ' + i + '.csv')
    print('Done exploding data')

explode_data(sourceFile, destinationFolder)