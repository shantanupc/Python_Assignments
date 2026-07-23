def CircleArea(R):
    return 3.14 * R * R

def main():
    Radius = int(input("Enter Radius of Circle: "))

    Ret = CircleArea(Radius)

    print("Area of Circle is: ",Ret)

if __name__ == "__main__":
    main()