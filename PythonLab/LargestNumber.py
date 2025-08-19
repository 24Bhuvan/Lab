def largest_num_in_array(li):
    ans=0
    for i in li:
        if i>ans:
            ans=i
    return ans
if __name__=="__main__":
    length = int(input("Enter length of array: "))
    li = []
    for i in range(length):
        x=int(input(f"Enter value of the element {i}: "))
        li.append(x)
    print(f"The Largest number in the array is {largest_num_in_array(li)}")