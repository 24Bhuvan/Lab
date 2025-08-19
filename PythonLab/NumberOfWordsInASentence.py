def Words_In_Sentence(Array):
    ans=0
    for i in Array:
        temp = 1
        for char in i:
            if char == " ":
                temp +=1
        ans = max(ans,temp)
    return ans
if __name__=="__main__":
    length = int(input("Enter Number of sentences: "))
    li = []
    for i in range(length):
        x=input(f"Enter Sentence {i+1}: ")
        li.append(x)
    print(f"The maximum number of words{Words_In_Sentence(li)}")