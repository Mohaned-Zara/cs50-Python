
print("Amount Due: 50")
due=50
while (True):
    x = int(input("Insert coin: "))
    if x == 5 or x == 10 or x ==25:
        if x == 50:
            break
        due = due - x
        if due<=0:
            if due == 0:
                print(f"Change Owed: {0}")
                break
            else:
                print(f"Change Owed: {due * -1}")
                break
        elif due>50:
            print(f"Change Owed: {due-50}")
        else:
            print(f"Amount Due: {due}")
    else:
        print("Amount Due:",due)
        break

"""
    Better Code:
"""
"""
print("Amount Due: 50")
due = 50
coins = [5,10,25]
while due > 0:
    x = int(input("Insert coin: "))

    if x in coins:
        due -= x

    if due > 0:
        print(f"Amount Due: {due}")
    else:
        print(f"Change Owed: {abs(due)}") 
"""