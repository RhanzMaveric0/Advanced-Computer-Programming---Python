import re

text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)

if match:
    print(f"Phone number found: {match.group()}")

print()

email_text = "Contact me at john@example.com for more info"
email_pattern = r"\w+@\w+\.\w+"
email_match = re.search(email_pattern, email_text)

if email_match:
    print(f"Email found: {email_match.group()}")

print()

numbers_text = "I have 5 apples, 10 oranges, and 3 bananas"
numbers = re.findall(r"\d+", numbers_text)
print(f"Numbers found: {numbers}")

print()

message = "Hello World! Welcome to World."
new_message = re.sub(r"World", "Python", message)
print(f"Original: {message}")
print(f"Replaced: {new_message}")
