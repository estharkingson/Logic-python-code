# Variables for demonstration
temperature = 25
is_raining = True
has_umbrella = False

# Using an if-elif-else statement
if temperature > 30:
    print("It's a hot day!")
elif temperature >= 20 and temperature <= 30:
    print("The weather is pleasant.")
else:
    print("It's a cold day.")

# Using logical operators
if is_raining and   not has_umbrella:
    print("You should find shelter!")
elif is_raining and has_umbrella:
    print("You're prepared for the rain.")
else:
    print("No rain today.")

# Another example with 'or'
age = 17
has_license = False

if age >= 18 or has_license:
    print("You can drive.")
else:
    print("You cannot drive yet.")
