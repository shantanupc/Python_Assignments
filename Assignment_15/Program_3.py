RetEven = lambda Num : Num % 2 != 0

def main():
    Data = [13,12,8,10,11,20]

    FData = list(filter(RetEven,Data))

    print(FData)

if __name__ == "__main__":
    main()