def main():
    Num = int(input("Enter a number: "))

    count = 0
    Digit = 0

    while(Num > 0):
        Num = Num // 10
        count = count + 1
    
    print(count)    

if __name__ == "__main__":
    main()