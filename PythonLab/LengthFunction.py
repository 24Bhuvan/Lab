def string_length(s):
    count =0
    for char in s:
        count+=1
    return count
input_string = input("Enter your string:")
length_of_string = string_length(input_string)
print(f"{length_of_string} is the length of your string")