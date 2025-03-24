def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if 2 <= len(plate) < 7:
        return False
    else:
        
        # check for Third digit not equal zero
        if plate[2] == "0" or plate[3] == "0":
            return False
        
        else:
        
            # check for first 3 characters 

            for char in plate[0:2]:
                if char.isalpha():
                    continue
                else:
                    print(char)
                    return False
        
            # check for last 3 characters
    
            for num in plate[3:]:
                if num.isdigit():
                    continue
                else:
                    print(num)
                    return False
            return True


main()
