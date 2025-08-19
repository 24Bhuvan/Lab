def test_location(cards,query,mid):
    if cards[mid] ==query:
        if mid-1>=0 and cards[mid-1]==query:
            return 'left' 
        else:
            return "found"
    elif cards[mid] < query :
        return "left"
    else:
        return "right"
    
def locate_card(cards,query):
    lo, hi = 0, len(cards)-1
    while lo<=hi :
        mid = (lo+hi)//2
        result = test_location(cards,query,mid)
        if result=='found':
            return mid
        elif result=="right":
            lo = mid+1
        elif result=="left":
            hi = mid-1
    return -1
if __name__=="__main__":
    n=int(input("Enter number elements: "))
    li=[]
    print("Enter Elements in descending order:")
    for i in range(n):
        x=int(input(f"Enterelement number{i}: "))
        li.append(x)
    query = int(input("Enter your query number: "))
    print(f"Position of the element is {locate_card(li,query)}")