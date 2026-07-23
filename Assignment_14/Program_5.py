CheckEven = lambda Num : True if Num % 2 == 0 else False

def main():
    No = int(input("Enter a number: "))

    Ret = CheckEven(No)    

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()