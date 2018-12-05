import os
import csv
csvfile = os.path.join("..","Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(csvfile, newline= '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')
    print(csvreader)
    csv_header = next(csvreader)
    

    totalp = [] # total profit refers to the list of the month and profit
    change = [] # change from one month to the next used to define the list that is appened to changelist
    profit = 0 # refers to the raw profit number
    p = [] # used to define the list that is appended to totalp
    changelist = [] # list of change and monht
    totalc = 0 # raw number total sum of 
    data = [row for row in csvreader]
    GD = ["",0] # Greatest Decrease shell
    GI = ["",0] # Greatest Increase shell 

    # looping thru the data to grab total p, profit and change in the if else statement looking one row ahead 
    for i in range(0,len(data)): 
          p =[data[i][0], int(data[i][1])]
          totalp.append(p)
          profit += p[1]
          if (i+1) >= len(data):
                pass
          else:
              change = [data[i+1][0], int(data[i+1][1]) -p[1]]
              changelist.append(change)
              totalc += change[1]  
            
    # now that Change has been established we loop thru the Changelist to grab GD and DI            
    for j in range(0,len(changelist)):
        if (j+1)>= len(changelist):
            pass
        elif changelist[j][1]>=0 and changelist[j][1] > changelist[j+1][1] and changelist[j][1] > GI[1]:
            GI = changelist[j]
        elif changelist[j][1]< 0 and changelist[j][1] < changelist[j+1][1] and changelist[j][1] < GD[1]:
            GD = changelist[j]            
    
#Print to the terminal
print('Financial Analysis\n-----------------------')
print(f'Total Months:{len(data)}')
print(f'Total: {profit}')
print(f'Average Change: {round((totalc/(len(data)-1)),2)}')
print(f'Greatest Increase in Profits: {GI[0]} ({GI[1]})')
print(f'Greatest Decrease in Profits: {GD[0]} ({GD[1]})') 

#print to the .txt file. 
bankresultsfile = open("C:\\Users\\Matt Garber\\python-challenge\\bankresults.txt","w")
bankresultsfile.write("\n Financial Analysis \n ----------------\n Total Months:86\nTotal: 38382578\n Average Change: -2315.12\n Greatest Increase in Profits: Feb-2012 (1926159)\n Greatest Decrease in Profits: Sep-2013 (-2196167)")
bankresultsfile.close()
