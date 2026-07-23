from functools import reduce

Add = lambda Num1, Num2 : Num1 if Num1>Num2 else Num2

def main():
    Data = [13,12,8,10,11,20]

    RData = reduce(Add,Data)

    print(RData)

if __name__ == "__main__":
    main()