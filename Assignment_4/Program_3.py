def NumSquare(Value):
    Sqr = Value * Value

    return Sqr

def main():
    Num = int(input("Enter a number: "))

    Ret = NumSquare(Num)

    print("Square of number is:",Ret)

if __name__ == "__main__":
    main()