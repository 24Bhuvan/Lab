def ScoreOfAString(s):
    ans=0
    for i in range(len(s)-1):
        ans=ans+abs(ord(s[i])-ord(s[i+1]))
    return ans
s=input("Enter your string:")
if __name__ =="__main__": 
    print(ScoreOfAString(s))