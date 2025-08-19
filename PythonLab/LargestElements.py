def largest_number():
    a = int(input("Enter your first number:"))
    b = int(input("Enter your second number:"))
    c = int(input("Enter your third number:"))
    if (a>b and a>c) :
        print(f"{a} is the largest number")
    elif (b>a and b>c) :
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")
if __name__ == "__main__":
    largest_number()