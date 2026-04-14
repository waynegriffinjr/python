# My first Python program
# This prints a personal introduction

print("=" * 40) # Prints a line of 40 equal signs
print("Personal Introduction")
print("=" * 40)

# Personal details stored as variables
first_name = "Wayne"
last_name = "Griffin Jr"
age = 37
city = "Cincinnati"
favorite_language = "Python" # Because we're learning it right now!

# Display the introduction
print("Name:", first_name, last_name)
print("Age:", age)
print("City:", city)
print("Favorite Language:", favorite_language)
print("=" * 40)

# f-strings let you embed variables directly in text
print(f"\n{first_name} is {age} years old and lives in {city}.")
print(f"He is currently learning {favorite_language} to build AI systems.")

