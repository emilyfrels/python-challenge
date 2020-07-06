# Import the os module
import os

# Import the module to read a csv file
import csv


# Set variable and location of csv file

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# Check to make sure the file path is correct
# print(csvpath)

# Set variable and location of output text file
output_path = os.path.join('analysis', 'financial_analysis_results.txt')

# Open the output file
with open(output_path, 'w') as txtfile:

    # Open the csv

    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',') 


        # Print the title and a spacer
        print("FINANCIAL ANALYSIS")
        print("------------------")
        txtfile.write("FINANCIAL ANALYSIS\n")
        txtfile.write("------------------\n")


        # Confirm we are reading the header row correctly
        # print(f"CSV Header: {csv_header}")

        # Need to skip the header in the CSV
        csv_header = next(csvreader)

        # Find the total number of months
        total_months = len(list(csvreader))

        # Print the total number of months in the list
        print(f"Total Months: {total_months}")
        txtfile.write(f"Total Months: {total_months}\n")

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
        txtfile.write(f"Total: ${total_pl}\n")

        # Create loop to go through each row in the Profit/Loss column to subtract
        # the previous month from the current month

    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',') 
        
        # Need to skip the header in the CSV
        csv_header = next(csvreader)
        next(csvreader)

        average_change = total_pl / total_months
        greatest_increase = max(row[1])
        greatest_decrease = min(row[1])


    print(f"Average Change: {average_change}")
    txtfile.write(f"Average Change: {average_change}\n")
    print(f"Greatest Increase in Profits: {greatest_increase}")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase}\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease}")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")

        
