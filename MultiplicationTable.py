def table():
    num = int(input("Enter the number:"))
    for i in range (1,11):
        print(f"{num}x{i}={num*i}")
if __name__ == "__main__":
    table()