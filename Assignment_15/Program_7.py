Strlen = lambda Str : len(Str) > 5

def main():
    Data = ["Shantanu","Swaraj","Rakshit","Bob","John"]

    FData = list(filter(Strlen,Data))

    print(FData)

if __name__ == "__main__":
    main()