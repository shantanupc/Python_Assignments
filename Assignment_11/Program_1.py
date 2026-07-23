def CheckPrime(n):

    IsPrime = False
    if n > 1:
        for i in range(2,n):
            if(n % i == 0):
                IsPrime = True
                break
        
    else:
        IsPrime = True

    return IsPrime
    
def main():
    Num = int(input("Enter a number: "))

    Ret = CheckPrime(Num)

    if(Ret == True):
        print("Number is not Prime")
    elif(Ret == False):
        print("Number is Prime")

if __name__ == "__main__":
    main()