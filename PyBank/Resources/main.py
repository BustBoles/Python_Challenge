import csv
# reading in data and making all of the code individual dictionaries
data = csv.DictReader(open('./Resources/budget_data.csv'))

months = 0 #creating variavbles and setting them equal to zerp
total = 0
pre_rev = 0
total_ch = 0
inc = 0


for row in data:  #calling the dictionaires by row 
    months += 1   #adding 1 to the months variable
    rev = int(row['Profit/Losses']) #declaring rev as an int the calling the numbers in the first dictionary
    total += rev  #

    ch = rev - pre_rev
    if pre_rev == 0:
        ch = 0

    total_ch += ch

    pre_rev = rev 
print(row)
 
 
 
 
    # if ch>int[1]:
    #     inc[1]= ch
    #     inc[0] = row['Date'] 


# output = f'''
# Financial Analysis
# ----------------------------
# Total Months: {months}
# Total: ${total:,}
# Average Change: ${total_ch/(months -1):,.2f}
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# '''

# print(output)