CheckOdd = lambda Num : True if Num % 2 != 0 else False

def main():
    No = int(input("Enter a number: "))

    Ret = CheckOdd(No)    

    if(Ret == True):
        print("Number is Odd")
    else:
        print("Number is Even")

if __name__ == "__main__":
    main()