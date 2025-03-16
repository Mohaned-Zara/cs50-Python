def main():
    x = input("enter greeting? ").lower()
    check_greeting(x)

def check_greeting(x):
    if x.find("hello") != -1:
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
