jug1 = 0
jug2 = 0
capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))
print("Jug1 Jug2")

while True:
    print(jug1, jug2)

    if jug1 == target or jug2 == target:
        print("Target reached")
        break

    if jug2 == 0:
        jug2 = capacity2
    elif jug1 < capacity1:
        transfer = min(jug2, capacity1 - jug1)
        jug1 += transfer
        jug2 -= transfer
    elif jug1 == capacity1:
        jug1 = 0
