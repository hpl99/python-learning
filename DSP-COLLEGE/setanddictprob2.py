employees = {
    1001: {"name": "Amit Kumar", "dept": "HR", "salary": 45000},
    1002: {"name": "Neha Singh", "dept": "IT", "salary": 60000},
    1003: {"name": "Ravi Patel", "dept": "IT", "salary": 52000},
    1004: {"name": "Pooja Mehta", "dept": "Marketing", "salary": 8000},
    1005: {"name": "Suresh Rao", "dept": "Operations", "salary": 55000}
}
depts = {}
for empid,data in employees.items():
    d = data["dept"]
    if d not in depts:
        depts[d]=[]
    depts[d].append(data["name"])

for d , names in depts.items():
    print(d,names)

for data in employees.values():
    if data["dept"] == "IT":
        data["salary"]=data["salary"]*0.1 + data["salary"]
        print(data["dept"],data["salary"]) 

maxsalary = 0
maxname= ""

for data in employees.values():
    if data["salary"] >  maxsalary:
        maxsalary = data["salary"]
        maxname = data["name"]

print(maxname,maxsalary)

print(1004 in employees) 

x= []

for empid , data in employees.items():
    if data["salary"]<20000:
        x.append(empid)
    
for empid in x:
    employees.pop(empid)

print(employees)

