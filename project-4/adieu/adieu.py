import inflect

def main():
    p = inflect.engine()
    names = []

    try:
        while True:
            names.append(input())
    except EOFError:
        pass

    joined = p.join(names)
    print(f"Adieu, adieu, to {joined}")

if __name__ == "__main__":
    main()
