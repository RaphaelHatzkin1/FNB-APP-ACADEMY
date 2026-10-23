
# grade_report.py

# List of students
students = [
    {"name": "Raphael", "maths": 78, "english": 82, "science": 75},
    {"name": "John", "maths": 65, "english": 70, "science": 68},
    {"name": "Sarah", "maths": 88, "english": 91, "science": 85},
    {"name": "Michael", "maths": 55, "english": 60, "science": 58},
    {"name": "Emily", "maths": 95, "english": 89, "science": 92}
]

# Empty list to store results
results = []

# Process each student
for student in students:
    # Calculate average
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Grade logic
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

    # Status logic
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Add result to results list
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })


# Calculate class statistics
class_average = sum(result["average"] for result in results) / len(results)

highest_mark = max(
    max(student["maths"], student["english"], student["science"])
    for student in students
)

lowest_mark = min(
    min(student["maths"], student["english"], student["science"])
    for student in students
)


# Display class report
print("\n" + "=" * 50)
print("             CLASS GRADE REPORT")
print("=" * 50)

for result in results:
    print(f"Name: {result['name']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")
    print("-" * 50)

# Display class statistics
print("\nCLASS STATISTICS")
print("=" * 50)
print(f"Class Average: {class_average:.2f}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print("=" * 50)


# Student search loop
while True:
    search_name = input("\nEnter a student name to search (or 'exit' to quit): ")

    if search_name.strip().lower() == "exit":
        print("Search ended. Goodbye!")
        break

    found = False

    for result in results:
        if result["name"].lower() == search_name.strip().lower():
            print("\nStudent Found!")
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']:.2f}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")
            found = True
            break

    if not found:
        print("Student not found. Please try again.")
