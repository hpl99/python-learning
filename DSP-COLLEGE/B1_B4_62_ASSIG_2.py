import json
import os
def add_result(name, marks):
    data = {}
    if os.path.exists("results.json"):
        with open("results.json", "r") as file:
            data = json.load(file)
    data[name] = marks 
    with open("results.json", "w") as file:
        json.dump(data, file)
def display_results():
    with open("results.json", "r") as file:
        data = json.load(file)
        for name, marks in data.items():
            print(f"{name}: {marks}")
def find_topper():
    with open("results.json", "r") as file:
        data = json.load(file)
    topper = max(data, key=data.get)
    print(f"Topper: {topper} with {data[topper]} marks")
add_result("raju", 85)
add_result("kaju", 92)
add_result("baju",99)
add_result("laju",100)
display_results()
find_topper()