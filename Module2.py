#Using a module
import Module1
Module1.greeting("Jonathan")
a = Module1.person1["age"]
print(a)

#Re-naming a Module
import Module1 as mx
a = mx.person1["age"]
print(a)

#Using the dir() Function
x = dir(Module1)
print(x)

#Import From Module
from  Module1 import person2
print (person2["age"])