#VARABLES AND DATA TYPES:
#Python has no command for declaring a variable.
def data_Types():
    """
Variables types:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
    name = "Bhuvan"
    age = 19
    score = 97.95
    is_student = True
    #Get the Type
    print(type(name))
    print(type(age))
    print(type(score))
    print(type(is_student))
    #Type Casting
    print(type(int(score)))
    print(type(str(age)))
    print(type(float(age)))
def Variable_Assigning():
    """
Variable Naming Rules:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
No Special Symbols
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
    #Many Values to Multiple Variable
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)
    #One Value to Multiple Variables
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)
    #Unpacking variables
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
if __name__=="__main__":
    data_Types()
    Variable_Assigning()
def Global_keyword():
  """
  GLOBAL VARIABLE- stays outside function and can be accessed by any function
  LOCAL VARIABLE-stays inside function and can be accessed by only defined function
  """
  global x #Converts local keyword to global keyword
  x = "fantastic"
if __name__=="__main__":
    Global_keyword()
print("Python is " + x)