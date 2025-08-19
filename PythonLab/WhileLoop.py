#WHILE LOOP:
def while_demo():
    """
The else Statement:
With the else statement we can run a block of code once when the condition no longer is true:
"""
    i = 1
    while i < 6:
        print(i)
        i+= 1
    else:
        print("i is no longer less than 6")
if __name__=="__main__": 
    while_demo() 
#For creating an empty block for defined functions,condtionals, loops use "pass"