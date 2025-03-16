def main():
    ask=input("What Time Is It? ")
    time,am_pm=ask.split(" ")
    hours, minutes = (time.split(":"))
#    print(hours, minutes,am_pm)
    convert(hours, minutes,am_pm)


def convert(hours,minutes,am_pm):
    int_hrs=int(hours)
    int_min=int(minutes)

    #breakfast: 7 --> 8
    if 7 <= int_hrs < 8 or (int_hrs == 8 and int_min == 00):
        print("Break-Fast Time")
    #lunch: 
    #dinner


if __name__ == "__main__":
    main()



