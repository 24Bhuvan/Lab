def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        sum = sum + ((temp%10)**3)
        temp=temp//10
    if sum ==num :
        return f"{num} is an Armstrong number"
    else:
        return f"{num} is not an armstrong number"
x= int(input("Enter your number:"))
print(armstrong(x))