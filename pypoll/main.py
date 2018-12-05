import os
import csv
csvfile = os.path.join("..","Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
with open(csvfile, newline= '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ',')
    print(csvreader)
    csv_header = next(csvreader)
    cd = ""
    count = 1
    tcount = 0
    lcount = 1
    vtcountlist = []
    data = [row[2] for row in csvreader]
    
    cdlist = []
    done = len(data)
    for i in range(0,len(data)):
        if data[i] not in cdlist:
            
            cd = data[i] 
        
            cdlist.append(cd)
    for j in range(0,len(cdlist)):
        for i in range(0,len(data)):
            if cdlist[j] == data[i]:
                count+=1
                vtcount = [cdlist[j],count]
           
        vtcountlist.append(vtcount) 
        count = 1                       
            
                  
       
     
        
        
        
        
        
        
        
    print('Election Results\n ----------------------')   
    print(f'Total Votes: {len(data)}\n --------------------')     
    print(f'{vtcountlist[0][0]}: {round(((vtcountlist[0][1]/len(data))* 100),2)}% ({vtcountlist[0][1]})')
    print(f'{vtcountlist[1][0]}: {round(((vtcountlist[1][1]/len(data))* 100),2)}% ({vtcountlist[1][1]})')
    print(f'{vtcountlist[2][0]}: {round(((vtcountlist[2][1]/len(data))* 100),2)}% ({vtcountlist[2][1]})')
    print(f'{vtcountlist[3][0]}: {round(((vtcountlist[3][1]/len(data))* 100),2)}% ({vtcountlist[3][1]})')  

resultsfile = open("C:\\Users\\Matt Garber\\python-challenge\\pollresults.txt","w")
resultsfile.write(("\n Election Results\n---------------------\n Total Votes: 3521001\n--------------------\nKhan: 63.0% (2218232)\nCorrey: 20.0% (704201)\nLi: 14.0% (492941)\nO'Tooley: 3.0% (105631)"))    
resultsfile.close()          