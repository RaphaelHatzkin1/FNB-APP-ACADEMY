
# Username and Message Formatter

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ")

# Create username: first initial + last name, all lowercase
username = first_name[0] + last_name
username = username.lower()

# Format full name using Title Case
full_name = (first_name + " " + last_name).title()

# Remove leading and trailing spaces from the bio
clean_bio = bio.strip()

# Count the number of characters in the bio
bio_length = len(clean_bio)

# Replace "I am" with "I'm"
formatted_bio = clean_bio.replace("I am", "I'm")

# Display the formatted profile
print("\n--- User Profile ---")
print(f"Full Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {formatted_bio}")
print(f"Bio Character Count: {bio_length}")
