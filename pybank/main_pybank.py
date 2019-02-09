import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'profits.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    
