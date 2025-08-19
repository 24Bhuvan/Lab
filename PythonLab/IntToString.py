def IntToString(i):
    digits="0123456789"
    if i == 0:
        return '0'
    result = ""
    while i>0:
        result = digits[i%10]+result
        i //= 10
    return result
if __name__=="__main__":
    x = int(input("Enter your integer:"))
    print(IntToString(x))