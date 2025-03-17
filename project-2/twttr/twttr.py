str = input("Input: ")
vowels = ["a", "e", "i","o", "u","A", "E", "I","O", "U"]
for c in str:
    if c in vowels:
        str=str.replace(c, "")
print(str)
