fruits = {"apple", "banana", "orange"}
print(f"Fruits set: {fruits}")

fruits.add("grape")
print(f"After adding grape: {fruits}")

numbers = {1, 2, 3, 2, 4, 1, 5}
print(f"Set removes duplicates: {numbers}")
print()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (all elements): {set1.union(set2)}")
print(f"Intersection (common elements): {set1.intersection(set2)}")
print(f"Difference (in set1 but not set2): {set1.difference(set2)}")
print()

if "apple" in fruits:
    print("Apple is in the set")

fruits.remove("banana")
print(f"After removing banana: {fruits}")
