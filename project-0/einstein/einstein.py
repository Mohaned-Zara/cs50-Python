def main():
    mass=int((input("M: ")))
    result = energy(mass)
    print(int(result))

def energy(M):
    Csqr = int(pow(300000000, 2))
    return (Csqr*M)


main()
