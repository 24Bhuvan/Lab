#EXCEPTION HANDLING
def divide_numbers(a, b):
  """
  This function divides two numbers and handles potential exceptions.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The result of the division if successful, 
    or an appropriate error message otherwise.
  """
  try:
    result = a / b  # Attempt the division
  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    return None
  except TypeError:
    print("Error: Input values must be numbers.")
    return None
  else:
    print("Division successful!")
    return result
  finally:
    print("This block always executes.")

# Example usage
num1 = 1
num2 = 0

result = divide_numbers(num1, num2) 

if result is not None:
  print("Result:", result)