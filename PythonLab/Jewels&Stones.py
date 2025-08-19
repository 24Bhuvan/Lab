def JewelStone(jewels,stone):
    ans=0
    for i in stone:
        for j in jewels:
            if i == j:
                ans +=1
                break
    return ans
if __name__=="__main__":
    jewels=input("Enter jewel characters:")
    stone=input("Enter Stone characters:")
    print(f"Number of jewels are :{JewelStone(jewels,stone)}")