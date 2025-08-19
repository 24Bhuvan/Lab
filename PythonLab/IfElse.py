#CONDITIONAL STATEMENTS:
a=int(input())
b=int(input())
def Short_Hand_If():
    """
    Short Hand If:
    If you have only one statement to execute, you can put it on the same line as the if statement.
    """
    if a > b: print("a is greater than b")
def Short_Hand_If_Else():
    """
Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
"""
    print("A") if a > b else print("B")
def Short_Hand_If_Else_Multiple():
    #You can also have multiple else statements on the same line:
    print("A") if a > b else print("=") if a == b else print("B")
if __name__=="__main__":  
    Short_Hand_If()
    Short_Hand_If_Else()
    Short_Hand_If_Else_Multiple()\
#For creating an empty block for defined functions,condtionals, loops use "pass"