def ChkGreater(Value1, Value2):
    if(Value1 > Value2):
        Greater = Value1
    else:
        Greater = Value2

    return Greater

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    Ret = ChkGreater(No1, No2)

    print(Ret,"is greater")

if __name__ == "__main__":
    main()