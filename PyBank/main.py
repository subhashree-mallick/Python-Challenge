#Dependencies
import os
import csv

#Intial Variables
total_months=0
total_profitloss=[]
net_profitloss=[]
greatest_increase_in_profit=["", 0]
greatest_decrease_in_profit=["",999999999]
total_amount=0

#files path associated with load and output
csvpath = os.path.join('Resources','budget_data.csv')
outputpath= os.path.join('Analysis','budget_analysis.txt')


#Open file in read mode
with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip the header
    csv_header=next(csvreader)
    #Extract first row to avoid appending to net profit loss
    first_row=next(csvreader)
    total_months+=1
    total_amount+= int(first_row[1])
    prev_net=int(first_row[1])
    

    #Read each row of data.
    for row in csvreader:
        total_months+=1
        total_amount=total_amount+int(row[1])
        #calculation for net change over the entire period
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        net_profitloss.append(net_change)
        #calculation for greatest increase in profit
        if net_change > greatest_increase_in_profit[1]:
           greatest_increase_in_profit[0]=row[0]
           greatest_increase_in_profit[1]=net_change
        #calculation for greatest decrease in profit
        if net_change < greatest_decrease_in_profit[1]:
           greatest_decrease_in_profit[0]=row[0]
           greatest_decrease_in_profit[1]=net_change   


    #calculate the average net change over a period
    net_monthly_change=sum(net_profitloss) /len(net_profitloss) 


with open(outputpath,"w") as txt_file:
    summary = (f"Financial Analysis\n"
                f"----------------------\n"
                f"Total Months: {total_months}\n"
                f"Total: $ {total_amount}\n"
                f"Average change: $ {net_monthly_change:.2f}\n"
                f"Greatest increase in profits: {greatest_increase_in_profit[0]} (${greatest_increase_in_profit[1]})\n"
                f"Greatest decrease in profits: {greatest_decrease_in_profit[0]} (${greatest_decrease_in_profit[1]})\n"
                )
    print(summary)            
    txt_file.write(summary)

    
       
   