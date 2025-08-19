def lcm():
    x=int(input("Enter your number1:"))
    y=int(input("Enter your number2:"))
    if x>y:
        num=x
    else:
        num=y
    while 1:
        if ((num%x==0)and(num%y==0)):
            lcm=num
            break
        num+=1
    print(f'{num} is the Least common multiple')
if __name__ == "__main__":
    lcm()