def main():
    Num = int(input("Enter a number: "))

    Digit = 0
    Sum = 0

    if(Num <= 0):
        print("Enter Positive numbers only")

    else:
        while(Num > 0):
            Digit = Num % 10
            Sum = Sum + Digit
            Num = Num // 10
    
        print(Sum)

if __name__ == "__main__":
    main()