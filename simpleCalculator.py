# Project Name: Simple Calculator
# Used Language: Python
# Submitted by: Abhi Udaya Dhungana, Class 7 'Beganas'
# School: Dimond Secondary School, Taalchowk, Pokhara 27, Kaski

# function to add two variables X and Y
def add(X, Y):
  return X + Y


# function to subtract variable Y from X
def sub(X, Y):
  return X - Y


# function to multiply two variables X and Y
def mul(X, Y):
  return X * Y


# function to divide variable X by Y
# Variable Y cannot be zero
def div(X, Y):
  # Conditional statement to check whether Y is zero
  if Y == 0:
    return "Error: Divide by zero error."
  else:
    return X / Y


def calculator():
   print('Simple Calculator')
   print('-----------------')
   print('1. Addition')
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")

   # User Input
   option = input("Choose one option [1-4]: ")

   if option in ('1','2','3','4'):
     # User inputs for calculations
     # Variables: number1 and number2
     number1 = int(input("Enter First Number: "))
     number2 = int(input("Enter Second Number: "))

     # Conditional Statements
     if option == '1':
      # Variable: result
      result = add(number1, number2)
      print(number1, " + ", number2, " = ", result)

     if option == '2':
      result = sub(number1,number2)
      print(number1, " - ", number2, " = ", result)

     if option == '3':
      result = mul(number1,number2)
      print(number1, " * ", number2, " = ", result)

     if option == '4':
      result = div(number1,number2)
      print(number1, " / ", number2, " = ", result)

   else:
     print("Error: Choose option number 1 to 4 only")


n = 1
# while loop statement to keep the calculation continue
# until user press N or n key to stop this application.
while n == 1:
  calculator()

  # User Input to continue or discontinue the calculation
  newCalculation = input("Do you want next calculation? (y/n)")

  if newCalculation == 'y' or newCalculation == 'Y':
    n = 1
  elif newCalculation == 'n' or newCalculation == 'N':
    n = n + 1

# End of the Code
