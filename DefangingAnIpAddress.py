def DefangIpAddr(address):
    ans=""
    for i in address:
        if i == ".":
            ans = ans+"[.]"
        else:
            ans = ans+i
    return ans
if __name__=="__main__":
    input_address=input("Enter the ip address:")
    print(DefangIpAddr(input_address))