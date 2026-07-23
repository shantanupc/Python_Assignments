def DecToBinary(Num):
    binaryNo = ""
    
    while(Num > 0):
        rem = Num % 2
        binaryNo = str(rem) + binaryNo
        Num = Num // 2

    return binaryNo

def main():
    No = int(input("Enter a number: "))

    Ret = DecToBinary(No)

    print(f"Binary equivalent of {No} is {Ret}")

if __name__ == "__main__":
    main()