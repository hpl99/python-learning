import json
import os
def add_expenses(item, amount):
    exp = []
    if os.path.exists("expense.json"):
        with open("expense.json", "r") as file:
            exp = json.load(file) 
    exp.append(amount)    
    with open("expense.json", "w") as file:
        json.dump(exp, file)
def total_expense():
    if os.path.exists("expense.json"):
        with open("expense.json", "r") as file:
            exp = json.load(file)
            print("TOTAL")
            print(sum(exp))
def highest_expense():
    if os.path.exists("expense.json"):
        with open("expense.json", "r") as file:
            exp = json.load(file)
            print(f"The highest expense is ")
            print(max(exp))
add_expenses("Milk", 55)
add_expenses("Bread", 30)
add_expenses("makhannn",99)
add_expenses("doodh",78)
total_expense()
highest_expense()