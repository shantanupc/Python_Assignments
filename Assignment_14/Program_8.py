Add = lambda Num1, Num2 : Num1 + Num2

def main():
    No1 = int(input("Enter first number: "))

    No2 = int(input("Enter second number: "))

    Ret = Add(No1,No2)    

    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()