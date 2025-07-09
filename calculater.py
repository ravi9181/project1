
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def sqrt(x):
    """Square root of a number"""
    if x < 0:
        return "Error: Cannot take square root of negative number!"
    return x ** 0.5

def calculator():
    """Main calculator function"""
    print("=== Python Calculator ===")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root (√)")
    print("7. Quit")
    
    while True:
        try:
            choice = input("\nEnter operation (1-7): ")
            
            if choice == '7':
                print("Thanks for using the calculator!")
                break
            
            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} × {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} ÷ {num2} = {result}")
                
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")
            
            elif choice == '6':
                num = float(input("Enter number: "))
                result = sqrt(num)
                print(f"√{num} = {result}")
            
            else:
                print("Invalid choice! Please enter 1-7.")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
