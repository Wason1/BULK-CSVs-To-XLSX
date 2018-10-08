# IMPORTING LIBRARIES -----------------------------------------------------------------------------------
#region
import pandas as pd
import os
import re
import glob
import csv
import shutil
#endregion


# INPUT VARIABLES----------------------------------------------------------------------------------------
#region

# Directory folder of the csv files you want to process
Input_path_CSVs = 'C:/FILES/OUTPUT_SORTED/Sewerage-Transfer-Monitoring-Plan/SPT/'

# Can change to xlsx if needed, other changes will be nessesary to code
Extension = 'csv'

# Csv files seperator for input and output files..generally (,) or (|)
Delimiter = '|'

# Output folder path of Report on Analysed files
Output_path_XLSX = 'C:/FILES/OUTPUT_SORTED/Sewerage-Transfer-Monitoring-Plan/'

print('Directories loaded...')

#endregion

# READ AND PROCESS THE CSV FILES-------------------------------------------------------------------------
#region
os.chdir(Input_path_CSVs)
filenames = [i for i in glob.glob('*.{}'.format(Extension))]
print(filenames)

bool_df_created = False
for filename in filenames:
    print(filename)
    if bool_df_created == False:
        df_file = pd.read_csv(filename, sep=Delimiter, dtype={'LOCATIONCODE': object, 'TEST_KEY_CODE': object})
        bool_df_created = True
        print('File Read')
    else:
        df_temp = pd.read_csv(filename, sep=Delimiter, dtype={'LOCATIONCODE': object, 'TEST_KEY_CODE': object})
        df_file = df_file.append(df_temp, sort=False)
        print('File Read')


print('_________________')
print('All Files Read...')
print('_________________')

#endregion

# CREATE EXCEL REPORT------------------------------------------------------------------------------------
#region
print(df_file.head(5))

print('Creating Excel File')
Report_path_filename = Output_path_XLSX + 'ALL-DATA.xlsx'
writer = pd.ExcelWriter(Report_path_filename)
df_file.to_excel(writer,'Sheet1', index=False)
writer.save()

print('_________________')
print('ALL DONE!')
print('_________________')

#endregion