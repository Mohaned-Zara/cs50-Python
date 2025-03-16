def main():
    camelcase=input("camelCase:- ")
    snake_case=""
    for char in camelcase:
        if char.isupper():
            temp ="_" + char.lower()
            snake_case = snake_case + temp
        else:
            snake_case= snake_case + char
    print("snake_case:- ",snake_case)

main()
