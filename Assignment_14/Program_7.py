FiveDivisibilityCheck = lambda Num : True if Num % 5 == 0 else False

def main():
    No = int(input("Enter a number: "))

    Ret = FiveDivisibilityCheck(No)    

    if(Ret == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")

if __name__ == "__main__":
    main()