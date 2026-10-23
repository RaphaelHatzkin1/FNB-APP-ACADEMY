
# South African Fuel Cost Calculator

kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("What is the petrol price per liter? R"))

# Calculate liters needed
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Display result rounded to 2 decimal places
print(f"Liters needed: {liters_needed}")
print(f"Total fuel cost: R{round(total_cost, 2)}")
