import math

text = "hello world"

print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title Case: {text.title()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('world', 'Python')}")
print()

number = 16.7

print(f"Original number: {number}")
print(f"Absolute value: {abs(-10)}")
print(f"Round: {round(number)}")
print(f"Square root: {math.sqrt(16)}")
print(f"Power: {pow(2, 3)}")
print(f"Max: {max(5, 10, 3)}")
print(f"Min: {min(5, 10, 3)}")
