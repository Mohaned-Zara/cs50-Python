def main():
    check_fuel()



def check_fuel():
    while True:
        try:
            x,y= input("Fraction: ").split(sep="/")
        except ValueError:
            pass

        try:
            x=int(x)
            y=int(y)
            try:
                z=round((x/y)*100)
                if z <= 1:
                    return print("E")
                elif 99 <= z <= 100 :
                    return print("F")
                elif z>100:
                    pass
                else:
                    return print(f"{z}%")

            except ZeroDivisionError:
                pass

        except (ValueError,UnboundLocalError):
            pass




main()
