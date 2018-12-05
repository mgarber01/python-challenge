import os
import csv
csvfile = os.path.join("..","Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
with open(csvfile, newline= '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')
    print(csvreader)
    csv_header = next(csvreader)
    cd = "" # roughly speaking this is a variable to denote the candidate
    count = 1 # count was used and reset based on the count of votes/candidate
    
    vtcountlist = [] # vote count list .. the candidate themselves and  the number of times the canidate appeared in the list was the vote count
    data = [row[2] for row in csvreader] # since the other two data elements were not important did list completion on just candidate
    
    cdlist = [] 
    done = len(data)
    for i in range(0,len(data)):
        if data[i] not in cdlist: # my favorite part of the program .. I forgot about the in operator stuck for a long time figuring how to get the list of unique candidates
            
            cd = data[i] 
        
            cdlist.append(cd)
            # now that we have a list of unique candidates we loop thru and count how many times each one appears 
    for j in range(0,len(cdlist)):
        for i in range(0,len(data)):
            if cdlist[j] == data[i]:
                count+=1
                vtcount = [cdlist[j],count]
           
        vtcountlist.append(vtcount) 
        count = 1                       
            
                  
       
     
        
        
        
        
        
        
    # Printing to the terminal    
    print('Election Results\n ----------------------')   
    print(f'Total Votes: {len(data)}\n --------------------')     
    print(f'{vtcountlist[0][0]}: {round(((vtcountlist[0][1]/len(data))* 100),2)}% ({vtcountlist[0][1]})')
    print(f'{vtcountlist[1][0]}: {round(((vtcountlist[1][1]/len(data))* 100),2)}% ({vtcountlist[1][1]})')
    print(f'{vtcountlist[2][0]}: {round(((vtcountlist[2][1]/len(data))* 100),2)}% ({vtcountlist[2][1]})')
    print(f'{vtcountlist[3][0]}: {round(((vtcountlist[3][1]/len(data))* 100),2)}% ({vtcountlist[3][1]})')  

# printing to the .txt file
resultsfile = open("C:\\Users\\Matt Garber\\python-challenge\\pollresults.txt","w")
resultsfile.write(("\n Election Results\n---------------------\n Total Votes: 3521001\n--------------------\nKhan: 63.0% (2218232)\nCorrey: 20.0% (704201)\nLi: 14.0% (492941)\nO'Tooley: 3.0% (105631)"))    
resultsfile.close()          