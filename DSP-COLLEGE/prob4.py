students = []
sports_club = set()
cultural_club = set()
fees_balance = {}
def add_student(roll_no, name, branch, fees):
    students.append((roll_no, name, branch))
    fees_balance[roll_no] = fees
def show_branch_wise(branch_name):
    for roll, name, branch in students:
        if branch.lower() == branch_name.lower():
            print(f"Roll: {roll} | Name: {name}")
def find_both_clubs():
    both = sports_club & cultural_club
    print(f"Both Clubs: {both}")
def show_low_balance():
    for roll, balance in fees_balance.items():
        if balance < 5000:
            print(f"Roll No: {roll} | Balance: {balance}")
add_student(101, "Alice", "CS", 4000)
add_student(102, "Bob", "IT", 6000)
add_student(103, "Charlie", "CS", 3000)
sports_club.update([101, 103])
cultural_club.update([103, 105])
show_branch_wise("CS")
find_both_clubs()
show_low_balance()