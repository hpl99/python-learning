students = {
    101: {"name": "ram", "marks": [85, 90, 88]},
    102: {"name": "bhaiya", "marks": [70, 75, 72]},
    103: {"name": "baban", "marks": [92, 95, 91]}
}
for rollno , det in students.items():
    total = sum(det["marks"])
    avg = (sum(det["marks"]))/3
    print(rollno,det["name"],total, avg)
for data in students.values():
    if sum(det["marks"])>80:
        print(data["name"])
students[104] = {"name": "David", "marks": [78, 82, 80]}
students[102]["marks"] = [80, 85, 88]
students.pop(101)
roll_no = 103
if roll_no in students:
    print("Exists")
else:
    print("Does not exists")
max_total = 0
top_student = ""
for data in students.values():
    total = max(data["marks"])
    if total>max_total:
        max_total = total
        top_student = data["name"]
print(top_student,max_total)