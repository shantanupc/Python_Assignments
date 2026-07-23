def main():
    Marks = int(input("Enter Marks: "))

    if(Marks >= 75 and Marks <= 100):
        print("Distinction")
    elif(Marks >= 60 and Marks < 75):
        print("First Class")
    elif(Marks >= 50 and Marks < 60):
        print("Second Class")
    elif(Marks >= 0 and Marks < 50):
        print("Fail")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()