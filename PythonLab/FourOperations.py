def FourOperations(code):
    x = 0
    for i in code:
        if i == "--X" or i == "X--":
            x -= 1
        elif i == "++X" or i == "X++":
            x += 1
        else:
            return "SyntaxError"
    return x

if __name__ == "__main__":
    Length = int(input("Enter the number of commands for your code: "))
    li = []
    for i in range(Length):
        temp = input(f"Enter value {i + 1} from ['--X', 'X--', '++X', 'X++']: ")
        li.append(temp)
    print(f"Your Code: {li}")
    print(f"Result: {FourOperations(li)}")
