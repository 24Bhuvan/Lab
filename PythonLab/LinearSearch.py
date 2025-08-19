def linear_search(li,query):
    position = 0
    while position<len(li):
        """The return statement in Python (and most programming languages) immediately exits the function and returns the specified value. 
        When the query is found, the return position statement is executed, and the function stops running at that point.
        """
        if li[position]==query:
            return position
        position +=1
    return -1
test ={"input":{
    "li":[13,11,10,7,4,3,1,0],
    "query":7},
    "output":3}
result = linear_search(test["input"]["li"],test["input"]["query"])
if result == test["output"] : 
    print(result)
else:
    print("Card not found")