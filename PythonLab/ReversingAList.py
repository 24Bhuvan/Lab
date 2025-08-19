def ReversingAList(x):
    for i in range (len(x)//2):
        other = len(x)-i-1
        temp = x[i]
        x[i]= x[other]
        x[other]=temp
    return x
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    print("Enter Elements in descending order:")
    for i in range(n):
        x=int(input(f"Enterelement number{i}: "))
        li.append(x)
    print(f"Reversed list: {ReversingAList(li)}")