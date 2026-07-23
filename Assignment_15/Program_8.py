CheckDivisibility = lambda Num : Num % 3 == 0 and Num % 5 == 0

def main():
    Data = [15,12,8,30,11,75]

    FData = list(filter(CheckDivisibility,Data))

    print(FData)

if __name__ == "__main__":
    main()