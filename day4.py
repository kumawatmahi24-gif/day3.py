# find the largest number among three numbers!
# here, ask user to enter three numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
#check if the first number is greater than or equal to both other numbers
if(num1>=num2)and(num1>=num3)
  largest =num1 #if both conditions are True, the first number is the largest
# if the first condition is False, check whether the second number is the largest
elif(num2>=num1)and(num2>=num3) 
  largest =num2 # Understand! if both conditions are True, the second number is the largest
else:
    largest =num3 # if neither the first nor second number is the largest, choose the third number
  #Finally, display the largest number using the print() statement.
  print("the largest number is:",largest)
        
