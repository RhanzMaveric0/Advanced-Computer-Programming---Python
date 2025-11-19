def add(x, y):
    return x + y

print(f"Regular function: {add(5, 3)}")

add_lambda = lambda x, y: x + y
print(f"Lambda function: {add_lambda(5, 3)}")

print()

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

is_even = lambda x: x % 2 == 0
print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

print()

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")
