import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

def months_counter(budget_data):
    with open(budget_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        total_months = sum(1 for row in csv_reader)  
    return total_months

def total(budget_data):
    with open(budget_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        total_sum = sum(float(row[1]) for row in csv_reader)  
    return total_sum

def average_change(budget_data):
    with open(budget_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        
        
        data = [float(row[1]) for row in csv_reader]
        
        
        changes = [data[i] - data[i-1] for i in range(1, len(data))]
        
       
        average = sum(changes) / len(changes)
    return average

def increase(budget_data):
    greatest_increase = 0
    increase_date = ''
    with open(budget_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        
        data = [(row[0], float(row[1])) for row in csv_reader]
        
        for i in range(1, len(data)):
            if data[i][1] - data[i-1][1] > greatest_increase:
                greatest_increase = data[i][1] - data[i-1][1]
                increase_date = data[i][0]
    return greatest_increase, increase_date

def decrease(budget_data):
    worst_increase = 0
    decrease_date = ''
    with open(budget_data, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        
        data = [(row[0], float(row[1])) for row in csv_reader]
        
        for i in range(1, len(data)):
            if data[i][1] - data[i-1][1] < worst_increase:
                worst_increase = data[i][1] - data[i-1][1]
                decrease_date = data[i][0]
    return worst_increase, decrease_date

total_months = months_counter(budget_data)
total_pl = total(budget_data)
average_pl = average_change(budget_data)
greatest_increase, increase_date = increase(budget_data)
worst_increase,decrease_date=decrease(budget_data)

print(f"Financial Analysis")
print(f"-"*25)
print(f'Total number of months: {total_months}')
print(f'Total: ${total_pl:,.2f}')
print(f'Average Change: ${average_pl:,.2f}')
print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase:,.2f})')
print(f'Greatest Decrease in Profits: {decrease_date} (${worst_increase:,.2f})')

folder= 'analysis'
analysis_file='analysis.txt'
analysis_path =os.path.join(folder,analysis_file)
with open(analysis_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-" * 25 + "\n")
    file.write(f'Total number of months: {total_months}\n')
    file.write(f'Total: ${total_pl:,.2f}\n')
    file.write(f'Average Change: ${average_pl:,.2f}\n')
    file.write(f'Greatest Increase in Profits: {increase_date} (${greatest_increase:,.2f})\n')
    file.write(f'Greatest Decrease in Profits: {decrease_date} (${worst_increase:,.2f})\n')