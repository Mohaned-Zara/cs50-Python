months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date=input("Date: ")
    if "/" in date:
        dm,dd,dy = date.strip().split("/")
        if dm.isdigit() and dd.isdigit() and dy.isdigit():
            month=int(dm)
            if month > 12 or month < 1:
                continue
            day=int(dd)
            if day > 31 or day < 1:
                continue
            year=int(dy)
            print(f"{year}-{month:02d}-{day:02d}")
            break
    elif "," in date:
        dmm,ddd,dyy = date.strip().split(" ")
        dddst=ddd.replace(",","")
        if not dmm.isdigit():
            day=int(dddst)
            if day > 31 or day < 1:
                continue
            year=int(dyy)
            if dmm in months:
                month=months.index(dmm)+1
                print(f"{year:02d}-{month:02d}-{day:02d}")
                break



"""
    try: #  mm / dd / yy
        month,day,year = input("Date: ").split("/")
        if month.isdigit():
            print(f"{year:02}-{month:02d}-{day:02d}")
            break
        else:
            try: #  mm / dd / yy
                month,day,year = input().split(" ")
                dayst = day.strip(",")
                if month in months:
                    print(f"{year:02}-{(months.index(month)+1):02}-{dayst:02}")
                    break
            except:
                pass
    except:
        pass
"""



