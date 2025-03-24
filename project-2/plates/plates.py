
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if len(plate) < 2 or len(plate) > 7:
        return False

    else:
        #check first ans second char is char
        if plate[0].isalpha() == False or plate[1].isalpha() == False:
            return False

        for i in range(len(plate)):
            if plate[i].isdigit():
                if plate[i] == "0":
                    return False
                if plate[i:].isdigit() == False:
                    return False
                break

        return True








"""

        if (plate[2].isalnum() == True and plate[2] == "0"):
            return False


            #check all char is char
        for allchar in plate[:]:
            if allchar.isalnum():
                return True
            else:
                break


            # check for first 2 characters
        for char in plate[0:2]:
            if char.isalpha():
                continue
            else:
                print(char,"char")
                return False

            # check for last 3 characters
        for num in plate[2:]:
            if num.isdigit():
                continue
            else:
                print(num)
                return False

        return True
"""



main()



