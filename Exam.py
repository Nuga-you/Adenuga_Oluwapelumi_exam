

# Question 1
# import math

def addition(a, b):
    return a + b 
def subtraction(a, b):
    return a - b 
def multiplication(a, b):
    return a * b 
def division(a, b):
    if b!=0:
        return a/b
    else:
        raise "error" 


print("*********Basic Calculator*******")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication(*)")
print("4. Division n(/)")
print("5. exit")

# Running
User_input=int(input("choose a number: "))
while True:
 try:
            if User_input== 1:
                number1=float(input("enter your first number: "))
                number2=float(input("enter your  second  number: "))
                print(f"Sum of {number1} and {number2}:", addition(number1, number2))

            elif User_input== 2:
                number1=float(input("enter your first number: "))
                number2=float(input("enter your  second  number: "))
                print(f"Difference btw {number1} and {number2}:", subtraction(number1, number2))

            elif User_input== 3:
                number1=float(input("enter your first number: "))
                number2=float(input("enter your  second  number: "))
                print(f"{number1} multiiplied by {number2}:", multiplication(number1, number2))

            elif User_input== 4:
                number1=float(input("enter your first number: "))
                number2=float(input("enter your  second  number: "))
                print(f"{number1} divided by {number2}:", division(number1, number2))
            elif User_input==5:
                print("Thank you ")
                break
            else:
                print("😔😔Sorry enter a valid option")
 except ValueError:
    print("enter a valid input")

#  Question 2

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break      # break out of loop
    num = int((user_input) )  # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
        print("goodbye")



# Question 3
while True:
    age = int(input("Enter your age (or type exit to quit): "))
    try:
          if age == exit:
            print("Goodbye! Thanks for checking")
            break
          if age >= 18 :
           print("You can vote")
          else:
           print("You cannot vote")
    except ValueError:
      print("Invalid input, Enter a digit")
      print("Goodbye!")




