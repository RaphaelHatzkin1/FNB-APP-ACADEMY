
# Student Grade Classifier

# Get learner's name
name = input("Enter learner's name: ")

# Get marks for three subjects
subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# Calculate average
average = (subject1 + subject2 + subject3) / 3

# Assign grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check for intervention
interventions = []

if subject1 < 40:
    interventions.append("Subject 1 needs intervention")

if subject2 < 40:
    interventions.append("Subject 2 needs intervention")

if subject3 < 40:
    interventions.append("Subject 3 needs intervention")

# Display report card
print("\n========== REPORT CARD ==========")
print(f"Learner Name: {name}")
print("---------------------------------")
print(f"Subject 1: {subject1:.2f}")
print(f"Subject 2: {subject2:.2f}")
print(f"Subject 3: {subject3:.2f}")
print("---------------------------------")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

# Display intervention messages
print("---------------------------------")

if len(interventions) > 0:
    print("Intervention Flags:")
    for intervention in interventions:
        print(f"- {intervention}")
else:
    print("Intervention Flags: None")

print("=================================")

