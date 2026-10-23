
# Multi-Function Calculator

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Basic arithmetic operations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display results
print("\n========== CALCULATOR RESULTS ==========")
print(f"Addition:       {addition:.2f}")
print(f"Subtraction:    {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")

# Check for division by zero
if num2 == 0:
    print("Division:       Cannot divide by zero")
    print("Floor Division: Cannot divide by zero")
    print("Modulus:        Cannot divide by zero")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"Division:       {division:.2f}")
    print(f"Floor Division: {floor_division:.2f}")
    print(f"Modulus:        {modulus:.2f}")

print("========================================")
