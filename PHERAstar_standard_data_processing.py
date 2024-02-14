# USAGE
# python PHERAstar_2x2_data_processing_v1.py data_path output_file plate_id_header

import os
from os import listdir
import csv
from datetime import datetime,date,timedelta
import pandas as pd
import math
import argparse

# Use argparser package to parse command line arguments
help_message = ''.join(['Script combines data from PHERAstar plate reader output files.', 
                        '\n', 
                        '\nPHERAstar export file name must be in the format: <ID1 | ID2 | ID3> <Protocol> <Date> <Time>.CSV'])    

parser = argparse.ArgumentParser(description=help_message, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-d", "--data", dest="data_path", help="Path to data files")
parser.add_argument("-o", "--output", dest="output_file", help="Name of output file")
parser.add_argument("-id", dest="plate_id_header", default="plate_ID", help="Header for plate ID column")
args = parser.parse_args()

data_path = args.data_path
output_file = args.output_file
plate_id_header = args.plate_id_header

# Get file and plate names
def getFiles(data_path):
    file_data = []
    file_names = os.listdir(data_path)
    for f in file_names:
        if f.split('.')[-1] == 'CSV':
            csv_data = [f, f.split(' ')[0], ' '.join(f.split('.')[0].split(' ')[2:4])]
            file_data.append(csv_data)

    print("\n")
    print("Data files found: " + str(len(file_data)))
    
    return file_data

# Parse protocol info from files
def parseInfo(file_data, file_data_df):
    wavelengths = []
    for file in file_data:
        file_path = "{}{}".format(data_path, file[0])

        # Get wavelength from third column of csv file using csv library
        data_sheet = []
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                data_sheet.append(row) 

        wavelength = data_sheet[0][2]
        wavelengths.append(wavelength)

    file_data_df['wavelengths'] = wavelengths
    # file_data_df = file_data_df[file_data_df['wavelengths'].str.contains("X1")]
    # get wavelengths between brackets in string
    file_data_df['wavelengths'] = file_data_df.wavelengths.str.split('(', expand = True)[1]
    # remove end bracket
    file_data_df['wavelengths'] = file_data_df.wavelengths.str.split(')', expand = True)[0]
    file_data_df['measurement'] = file_data_df[1] + '_' + file_data_df['wavelengths'].astype(str)
    file_data_df['datetime'] = pd.to_datetime(file_data_df[2], format = "%y-%m-%d %H-%M-%S")

    return file_data_df

# Print ordered data info
def printInfo(file_data_df):
    print("Plates measured: " + ", ".join(str(plate) for plate in file_data_df[1].unique()))
    print("Wavelengths measured: " + ", ".join(str(wave) for wave in file_data_df['wavelengths'].unique()))

def sortData(file_data_df, plate_list):
    sorted_data_list = [['file_name', 'plate_id', 'time', 'wavelength', 'plate_ID', 'datetime', 'timepoint']]
    timepoint_list = []
    for plate in plate_list:
        plate_df = file_data_df[file_data_df['measurement'] == plate]
        plate_df = plate_df.sort_values(by = 'datetime')
        plate_file_list = plate_df.values.tolist()
        for file in plate_file_list:
            file.append(str('T' + str(math.floor(plate_file_list.index(file)))))
            timepoint_list.append(str('T' + str(math.floor(plate_file_list.index(file)))))
        sorted_data_list.extend(plate_file_list)

    print("Timepoints measured: " + ", ".join(set(timepoint_list)))

    return sorted_data_list

def sorted384_standard(sorted_data_list):
    # Build sorted output file
    OD_data = [['measurement_ID', plate_id_header, 'timepoint', 'time', 'datetime', 'wavelength', 'well', 'value']]
    # FI_data = [['ID1', 'timepoint', 'time', 'datetime', 'well', 'sample', '355/460', '485/520', '500/545', '540/590', '575/610']]

    for file in sorted_data_list[1:]:
        with open(data_path + file[0], encoding='unicode_escape') as csv_file:
            csv_list = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                csv_list.append(row)

            # Get data from csv file excluding headers
            for data_row in csv_list[1:]:
                data_row = [file[4], file[1], file[6], file[2], file[5], file[3], data_row[0], data_row[2]]
                OD_data.append(data_row)
    
    return OD_data

# Run functions
def __main__(data_path = data_path):
    
    file_data = getFiles(data_path)

    file_data_df = pd.DataFrame(file_data)

    file_data_df = parseInfo(file_data, file_data_df)
    printInfo(file_data_df)

    plate_list = list(pd.unique(file_data_df['measurement']))

    sorted_data_list = sortData(file_data_df, plate_list)

    OD_data = sorted384_standard(sorted_data_list)

    return OD_data

OD_data = __main__()
            
# Open output file for writing
with open(output_file, 'w') as writeFile:
    writer = csv.writer(writeFile)
    for row in OD_data:
        writer.writerow(row)
        
print("Generated output: " + output_file)
print("\n")
