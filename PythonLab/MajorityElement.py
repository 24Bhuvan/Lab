def MajorityElement(arr):
    temp = len(arr)//2
    dici={}
    ans= 0
    for i in arr:
        if i not in dici:
            dici[i]=1
        else:
            dici[i]=dici[i]+1
    for i in dici:
        if temp < dici[i]:
            ans = i
            break
    return ans
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    for i in range(n):
        x=input(f"Enter item {i}: ")
        li.append(x)
    print(f"The element which occured most number of times is {MajorityElement(li)}")