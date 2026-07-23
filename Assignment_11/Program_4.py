def main():
    Num = int(input("Enter a number: "))

    Digit = 0
    NewNum = ""

    while(Num > 0):
        Digit = Num % 10
        NewNum = NewNum + str(Digit)
        Num = Num // 10

    NewNum2 = int(NewNum)
    print(NewNum2)

if __name__ == "__main__":
    main()