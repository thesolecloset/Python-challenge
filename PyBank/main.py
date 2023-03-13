#Import the necessary libraries
import csv
import os

#Declare all variables needed
NumMonths = 0
TotalMonths = 0
AvgChange = 0
ChangingMonth = 0
ChangingSum = 0
GreatestIncrease = 0
GreatestDecrease = 0
GreatestIncreaseMonth = 0
GreatestDecreaseMonth = 0
Dates = []
Changes = []

#Set the path of the CSV file that will have data pulled from
csvpath = "Resources/budget_data.csv"

#Open the CSV File & Read Data From It Using A Delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    #Find header line and skip it
    csv_header = next(csvreader)

    #Start pulling data from CSV file to manipulate it into the required categories
    for row in csvreader:
        Date = row[0]
        Change = row[1]
        Dates.append(Date)
        Changes.append(Change)

        #Calculate the Total Months & Total
        NumMonths = NumMonths + 1
        TotalMonths = TotalMonths + int(row[1])

#For loop & If statement to get the Average Change & Sum To Figure Out The Increase & Decrease In Profit
for ChangingMonth in range (NumMonths-1):
    AvgChange = AvgChange + (float(Changes[ChangingMonth+1]) - float(Changes[ChangingMonth])) 
    ChangingSum = (float(Changes[ChangingMonth+1]) - float(Changes[ChangingMonth])) 

    #If Statement to get Greatest Increase
    if ChangingSum > GreatestIncrease:
        GreatestIncrease = ChangingSum
        GreatestIncreaseMonth = ChangingMonth
    else:
        GreatestIncrease = GreatestIncrease

    #If Statement to get Greatest Increase
    if ChangingSum < GreatestDecrease:
        GreatestDecrease = ChangingSum
        GreatestDecreaseMonth = ChangingMonth
    else:
        GreatestDecrease = GreatestDecrease

#Print out the results of the data pulled
print ("Financial Analysis")
print ("")
print ("-------------------------------")
print ("")
print (f'Total Months:  {NumMonths}')
print (f'Total:  ${TotalMonths}')
print ("Average Change:  $" '{:.2f}'.format(AvgChange/(NumMonths-1),2))
print ("Greatest Increase In Profits: " + str(GreatestIncreaseMonth) + " ("+ '{:.0f}'.format(GreatestIncrease+1)+ ")")
print ("Greatest Decrease In Profits: " + str(GreatestDecreaseMonth) + " ("+ '{:.0f}'.format(GreatestDecrease+1)+ ")")


#Declare the output file we want to write the above results to & write to that file
output_file = "output.txt"
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow([])
    writer.writerow(["-------------------------------"])
    writer.writerow(["Total Months: " + str(NumMonths)])
    writer.writerow(["Total: $" + str(TotalMonths)])
    writer.writerow(["Average Change: $" '{:.2f}'.format(AvgChange/(NumMonths-1),2)])
    writer.writerow(["Greatest Increase In Profits: " + str(GreatestIncreaseMonth) + " (" + str(GreatestIncrease+1) + ")" ])
    writer.writerow(["Greatest Decrease In Profits: " + str(GreatestDecreaseMonth) + " (" + str(GreatestDecrease+1) + ")" ])