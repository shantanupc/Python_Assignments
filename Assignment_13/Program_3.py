def NumFact(No):
    factors = []

    for i in range(1, No+1):
        if No % i == 0:
            factors.append(i)
    
    return factors

def PerfectNum(No,RetFact):
    Sum = 0

    for no in RetFact:
        Sum = Sum + no

    if Sum == No:
        return True
    else:
        return False

def main():
    Num = int(input("Enter a number: "))

    RetFact = NumFact(Num)

    RetPerfect = PerfectNum(Num, RetFact)

    if RetPerfect == True:
        print("Perefect number")
    else:
        print("Not Perfect number")

if __name__ == "__main__":
    main()