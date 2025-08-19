def swap():
    a = int(input("Enter your first number:"))
    b = int(input("Enter your second number:"))
    x=0
    if a == 0:
        a=b
        b=0
    elif b == 0:
        b=a
        a=0
    else :
        x=a
        a=b
        b=x
    print(f"After Swapping 'YOUR FIRST NUMBER' = {a} and 'YOUR SECOND NUMBER' = {b} ")
if __name__ == "__main__":
    swap()