#Check whether a number is positive negative or zero.

#ask the user to enter a number
num=int(input("Enter the number:"))

#Check if the number is greater than zero
if num > 0:
  print("This is a positive number.")
#if the first condition is False, check if the number is less than zero
elif num < 0:
  print("This is a negative number.")

#if both conditions are False, the number must be zero
else:
  print("This is zero.")
