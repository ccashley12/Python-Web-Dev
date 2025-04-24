num1 = float (input("Enter first number: "))
num2 = float (input("Enter second number: "))
operator = input("Enter the operator (+ or -): ")

if operator == "+":
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)

elif operator == "-":
    result = num1 - num2
    print("The difference of", num1, "and", num2, "is", result)

else: 
    print("Uknown operator!")