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

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Need to skip the header in the CSV
    csv_header = next(csvreader)

    # Create variable and set intial value for total Profit/Loss
    total_pl = 0

    # Create loop to go through each row in the Profit/Loss column to add total
    for row in csvreader:
        
        # Loop through each row to find the value and add to the previous
        total_pl = total_pl + int(row[1])

     # Print the total Profit/Loss
    print(f"Total: ${total_pl}")

    # Create loop to go through each row in the Profit/Loss column to subtract
    # the previous month from the current month

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Need to skip the header in the CSV
    csv_header = next(csvreader)

    # Create loop to go through each row 
    for row in csvreader:
        
        # Loop through each row to find the value and add to the previous
        total_pl = total_pl + int(row[1])

     # Print the total Profit/Loss
    print(f"Total: ${total_pl}")


    # Create variables and set initial values
    average = 0
    total_average = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Need to skip the header in the CSV
    # csv_header = next(csvreader)
    next(csvreader)


    # Need to skip the first row because there will be no average at the beginning
    # next(csvreader)


    for row in csvreader:

        # Loop through first and second row to find the two values
        current_row = 0
        current_row = int(row[1])
        print(f"This is the row {current_row}")
        # next
        # next_row = 0
        # next_row = int(row[1])
        # print(f"This is the next row: {next_row}")
        # total = current_row + next_row
        # print(f"This is the current row + the next row: {total}")
        next
        print(next)
        #next_row = current_row + next(row[1])

        #profit_loss = [row[1]]
        #print(profit_loss)

    # for next_row_in_column in csvreader:

    #     next_row = 0
    #     next_row = int(row[1])
    #     print(f"This is the next row {next_row}")

    # add_rows = int(current_row) + int(next_row)
    # print(f"Total of every 2 rows: {add_rows}")   

        #next_row = next(csvreader)
        #next_row = int(row[1])
        # next_row = next(row[1])
        # print(f"This is the next row {next_row}")

        #row_1_row_2 = int(row[1]) + next

        # average = average + int(row[1]) / 2
        # next_row = int(row[1])
        # row1 = int(row[1])
        # row2 = next(row[1])

        #print(average)
        #print(next_row)
        # print(f"Row 1: {row1}")
        # print(row2)

        # average = 0

        #next

    #     break
        
    #     total_average = total_average + average
    
    # print(average)
        

    # print(total_average)
    
