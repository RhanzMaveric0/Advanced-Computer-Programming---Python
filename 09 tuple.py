fruits = ("apple", "banana", "orange")
print(f"Fruits tuple: {fruits}")

print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print()

person = ("John", 25, "New York")
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print()

numbers = (1, 2, 3, 2, 4, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")
print()

my_list = [1, 2, 3]
my_list[0] = 10
print(f"List (mutable): {my_list}")

my_tuple = (1, 2, 3)
print(f"Tuple (immutable): {my_tuple}")
