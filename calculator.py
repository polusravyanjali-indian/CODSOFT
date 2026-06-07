# CodSoft Task 2 - Calculator
# Created by: Polu Sravyanjali

def calculator():
    print("=" * 30)
    print("   SIMPLE CALCULATOR")
    print("=" * 30)
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("\nEnter choice (1/2/3/4): ")
    
    if choice == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("\nError! Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid choice!")

while True:
    calculator()
    again = input("\nCalculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Thank you! Goodbye!")
        break