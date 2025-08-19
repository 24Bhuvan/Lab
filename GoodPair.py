def GoodPair(arr):
    ans = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] ==arr[j]:
                ans+=1
    return ans
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    for i in range(n):
        x=input(f"Enter item {i}: ")
        li.append(x)
    print(f"The number of Good Pairs : {GoodPair(li)}")