# day3.py
Calculate factorial of a number.
def factorial(n):  #def = Creates a function 
if n==0 or n==1:# Because factorial of 0 and 1 is always 1
    return 1 # sends a result back 
# otherwise, multiply n by the factorial of n-1
  else:
    return n * factorial(n-1) # this is called recursion it means the function calls itself to solve a smaller version of the same problem.
    # Enter the number by user
num =int(input("Enter the number:")) #int() converts the entered value into an integer
# Call the factorial function and display the result
print("factorial:", factorial(num))
  
