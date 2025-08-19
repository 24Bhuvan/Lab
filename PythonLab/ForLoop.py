#For loops
def for_demo():
    """
    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    """
    #Print each fruit in a fruit list:
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
    #Loop through the letters in the word "banana":
    for x in "banana":
        print(x)
def for_demo_break():
    #find the difference in below code 1 and 2
    #1
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break
    #2
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)
    #Similarly you can use continue too
def for_else():
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")
def for_range():
    for x in range(2, 30, 3):
        print(x)
if __name__=="__main__":
    for_demo()
    for_demo_break()
    for_else()
    for_range()