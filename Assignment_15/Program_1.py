Sqr = lambda Num : Num*Num

def main():
    Data = [13,12,8,10,11,20]

    MData = list(map(Sqr,Data))

    print(MData)

if __name__ == "__main__":
    main()