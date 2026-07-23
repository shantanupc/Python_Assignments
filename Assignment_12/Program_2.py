def NumFact(No):
    factors = []

    for i in range(1, No+1):
        if No % i == 0:
            factors.append(i)
    
    return factors

def main():
    Num = int(input("Enter a number: "))

    Ret = NumFact(Num)

    print(Ret)

if __name__ == "__main__":
    main()