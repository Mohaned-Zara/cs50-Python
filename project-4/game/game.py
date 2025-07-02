import random

def main():
        
    while True:
        try: 
            level = int(input("Level:"))
            if level > 0:
                break

            while(level <= int(0)):
                level = int(input("Level:"))
        except ValueError:
            pass

    random_number = random.randint(1, level)

    while True:
        try: 
            guess = int(input("guess:"))
            while(guess <= int(0)):
                guess = int(input("guess:"))

            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")  
                break  
        except ValueError:
            pass



if __name__=="__main__":
    main()