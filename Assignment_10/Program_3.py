def Factorial(Num):
    Fact = 1

    if(Num < 0):
        return -1
    else:
        for i in range(1,Num+1):
            Fact = Fact * i
        return Fact

def main():
    No = int(input("Enter a number: "))

    Ret = Factorial(No)

    if(Ret == -1):
        print("Factorial does not exist for negative number")
    else:
        print("Factorial is:",Ret)

if __name__ == "__main__":
    main()