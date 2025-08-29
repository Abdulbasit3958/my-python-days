# SET = Collection of unique elements, unordered

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Add element
fruits.add("mango")
print(fruits)

# Remove element
fruits.remove("banana")
print(fruits)

# Sets automatically ignore duplicates
fruits.add("apple")
print(fruits)  # "apple" won’t appear twice
