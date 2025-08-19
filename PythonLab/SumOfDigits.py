in_put=int(input())
sum=0
temp=in_put
while temp>0:
    sum = sum +(temp%10)
    temp=temp//10
print(sum)