import csv 

total_months = 0
total_profit = 0
average_change = 0
great_increase = 0
great_decrease = 0
great_increase_date = ""
great_decrease_date = ""
monthly_changes = []
previous_profit = 0

csvpath = "/Users/Xenos/Desktop/PythonChallenge/python-challenge/PyBank/Resources/budget_data.csv"
output_file = "/Users/Xenos/Desktop/PythonChallenge/python-challenge/PyBank/financial_analysis.txt"

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
                
                  if monthly_change > great_increase:
                    great_increase = monthly_change
                    great_increase_date = row[0]
                  elif monthly_change < great_decrease:
                    great_decrease = monthly_change 
                    great_decrease_date = row[0]

            previous_profit = int(row[1])

average_change = sum(monthly_changes)/len(monthly_changes)


print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profit: {great_increase_date} (${great_increase})")
print(f"Greatest Decrease in Profit: {great_decrease_date} (${great_decrease})")

with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profit: {great_increase_date} (${great_increase})\n")
    file.write(f"Greatest Decrease in Profit: {great_decrease_date} (${great_decrease})\n")

print("Financial Analysis has been saved to 'financial_analysis.txt'")

