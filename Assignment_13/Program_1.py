def RectArea(L,B):
    return L*B

def main():
    Length = int(input("Enter Length of rectangle: "))
    Width = int(input("Enter Width of rectangle: "))

    Ret = RectArea(Length, Width)

    print("Area of Rectangle is: ",Ret)

if __name__ == "__main__":
    main()