student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "city": "New York"
}

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print()

student["email"] = "john@email.com"
print(f"Updated dictionary: {student}")
print()

student["age"] = 21
print(f"New age: {student['age']}")
print()

del student["city"]
print(f"After removing city: {student}")
print()

print(f"All keys: {student.keys()}")
print(f"All values: {student.values()}")
print(f"All items: {student.items()}")
