#Dependencies
import os
import csv
# Load and output file path.
csvpath= os.path.join('Resources','election_data.csv')
outputpath=os.path.join('Analysis','election_analysis.txt')
#Initialize the variables
total_votes=0
candidate_list=[]
candidate_votes={}
winning_vote_count=0
winner=""

#Reading csv file
with open (csvpath,'r')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #read the header
    csvheader=next(csvreader)
    # print(csvheader)

    #For each row...
    for row in csvreader:
        #Add to the total vote count
        total_votes=total_votes+1
        #Extract the candidate name from each row
        candidate_name=row[2]
        #getting all the candidate name
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 

with open(outputpath,"w") as outputfile: 
    results=(f"Election Results\n"
             f"-----------------------\n"
             f"Total Votes : {total_votes}\n"
             f"-------------------------\n")   
    print(results) 
    outputfile.write(results)          

    #for loop for winning candidate
    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        vote_percentage= float(votes /total_votes)*100 
        voteresult=(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(voteresult)
        outputfile.write(voteresult)   

        if (votes > winning_vote_count):
            winning_vote_count = votes 
            winner=candidate  

    winningteam=(f"-------------------------\n"
                 f"winner : {winner}\n"
                 f"-------------------------") 
    print(winningteam)
    outputfile.write(winningteam)
      