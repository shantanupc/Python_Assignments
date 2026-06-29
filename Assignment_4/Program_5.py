def CheckDivisibility(Value):
    if(Value % 3 == 0 and Value % 5 == 0):
        return 8
    elif(Value % 3 == 0):
        return 3
    elif(Value % 5 == 0):
        return 5
    else:
        return 0

def main():
    Num = int(input("Enter a number: "))

    Ret = CheckDivisibility(Num)

    if(Ret == 8):
        print("Number is divisible by both 3 and 5")
    elif(Ret == 3):
        print("NUmber is divisible by 3 but not 5")
    elif(Ret == 5):
        print("Number is divisible by 5 but not 3")
    elif(Ret == 0):
        print("Number is not divisible by 3 nor 5")

if __name__ == "__main__":
    main()