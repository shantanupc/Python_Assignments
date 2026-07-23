def SumNaturalNumbers(n):
    SumNaturalNo = (n*(n+1))/2

    return SumNaturalNo

def main():
    Num = int(input("Enter a number: "))

    Ret = SumNaturalNumbers(Num)

    print(Ret)

if __name__ == "__main__":
    main()