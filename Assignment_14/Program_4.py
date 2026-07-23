MinNum = lambda Num1, Num2 : Num1 if Num1 < Num2 else Num2

def main():
    No1 = int(input("Enter first number: "))

    No2 = int(input("Enter second number: "))

    Ret = MinNum(No1,No2)    

    print("Minimum number is: ",Ret)

if __name__ == "__main__":
    main()