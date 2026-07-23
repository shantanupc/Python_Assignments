MaxNum = lambda Num1, Num2, Num3 : Num1 if(Num1>Num2 and Num1>Num3) else(Num2 if Num2>Num1 and Num2>Num3 else Num3)

def main():
    No1 = int(input("Enter first number: "))

    No2 = int(input("Enter second number: "))

    No3 = int(input("Enter third number: "))

    Ret = MaxNum(No1,No2,No3)    

    print("Maximum number is: ",Ret)

if __name__ == "__main__":
    main()