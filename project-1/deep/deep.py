x = input ("“The Answer to the Great Question Of Life,\
     the Universe and Everything is? ").strip().lower().replace("-"," ")
match x:
    case "42":
        print("yes")
    case "forty two":
        print("yes")
    case _:
        print("no")


