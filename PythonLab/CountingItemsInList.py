def Counting_items(arr):
    dici={}
    for i in arr:
        if i not in dici:
            dici[i]=1
        else:
            dici[i]=dici[i]+1
    return dici
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    for i in range(n):
        x=input(f"Enter item {i}: ")
        li.append(x)
    print(f"The number of times an item repeated is : {Counting_items(li)}")