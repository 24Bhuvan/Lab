def vowels(x):
    counts=['a','e','i','o','u']
    count=0
    for char in x:
        if char in counts:
            count+=1
    print(f'Number of vowels are {count}')
x= input("Enter Your String:")
if __name__ == "__main__":
    vowels(x)