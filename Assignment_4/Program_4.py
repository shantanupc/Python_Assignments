def NumCube(Value):
    Cube = Value * Value * Value

    return Cube

def main():
    Num = int(input("Enter a number: "))

    Ret = NumCube(Num)

    print("Cube of number is:",Ret)

if __name__ == "__main__":
    main()