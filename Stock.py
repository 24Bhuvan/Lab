def Buying_and_selling_stock(price):
    ans =0
    n=len(price)
    for i in range(n):
        for j in range(i+1,n):
            temp = abs(price[i]-price[j])
            ans = max(ans,temp)
    return ans
if __name__=="__main__":
    length = int(input("Enter Number of Days to be calculated: "))
    li = []
    for i in range(length):
            x=int(input(f"Enter Day {i+1} price: "))
            li.append(x)
    print(f"The maximum profit is {Buying_and_selling_stock(li)}")