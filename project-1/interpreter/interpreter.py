exp = input("Expression: ")
x,y,z =exp.split(" ")
x=int(x)
z=float(z)
match y :
    case "*":
        print(x * z)
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        if z != 0:
            print(x/z)
        else:
            print("Error 404")

