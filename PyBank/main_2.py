# Import the os module
import os

# Import the module to read a csv file
import csv


# Set variable and location of csv file

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# Check to make sure the file path is correct
# print(csvpath)

# Open the csv



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Check to make sure file is being read
    # print(csvreader)

    # Print the title and a spacer
    print("FINANCIAL ANALYSIS")
    print("------------------")


    # Confirm we are reading the header row correctly
    # print(f"CSV Header: {csv_header}")

    # Need to skip the header in the CSV
    csv_header = next(csvreader)

    # Find the total number of months
    total_months = len(list(csvreader))

    # Print the total number of months in the list
    print(f"Total Months: {total_months}")

change_in_pnl = []
row_1 = 0
row_2 = 0

#skip the first row because there will be no change
next(csvreader)
change_in_PNL = row_2 - row_1