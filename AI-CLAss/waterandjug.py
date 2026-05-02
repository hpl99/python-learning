def manual_water_jug(A, B, goal):
    a, b = 0, 0
    def show():
        print(f"Jug A: {a}/{A}, Jug B: {b}/{B}")
    print("Water Jug Problem (Manual Mode)")
    print("Operations:")
    print("1.Fill A  " \
    "      2.Fill B  " \
    "      3.Empty A  " \
    "      4.Empty B  " \
    "      5.Pour A->B  " \
    "      6.Pour B->A  " \
    "      0.Exit")
    while True:
        show()
        if a == goal or b == goal:
            print("Goal reached!")
            break
        op = int(input("Choose operation: "))
        if op == 1:
            a = A
        elif op == 2:
            b = B
        elif op == 3:
            a = 0
        elif op == 4:
            b = 0
        elif op == 5:
            transfer = min(a, B - b)
            a -= transfer
            b += transfer
        elif op == 6:
            transfer = min(b, A - a)
            b -= transfer
            a += transfer
        elif op == 0:
            print("Exited.")
            break
        else:
            print("Invalid operation")
manual_water_jug(8,5,4)