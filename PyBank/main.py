import csv 

total_months = 0
total_profit = 0
average_change = 0
great_increase = 0
great_decrease = 0
monthly_changes[]

csvpath = "/Users/Xenos/Desktop/PythonChallenge/python-challenge/PyBank/Resources/budget_data.csv"

with open(csvpath) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")
    budget_header = next(csv_reader)
    print(budget_header)
    
    for row in csv_reader:
            total_months += 1
            total_profit += int(row[1])

            if total_months > 1:
                  monthly_change = int(row[1]) - previous_profit
                  monthly_changes.append(monthly_change)



    

print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
