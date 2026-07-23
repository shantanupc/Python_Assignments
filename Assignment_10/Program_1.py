def main():
    Num = int(input("Enter a number: "))

    print("Multiplication table of",Num,"is")
    for i in range(Num,Num*11,Num):
        print(i)

if __name__ == "__main__":
    main()