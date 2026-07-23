def main():
    Num = int(input("Enter a number: "))
    
    NumCl = Num
    Digit = 0
    NewNum = ""

    while(NumCl > 0):
        Digit = NumCl % 10
        NewNum = NewNum + str(Digit)
        NumCl = NumCl // 10

    NewNum2 = int(NewNum)

    if(NewNum2 == Num):
        print("Palindrome")
    else:
        print("Not Palindrome")    

if __name__ == "__main__":
    main()