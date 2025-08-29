# LIST = Collection of items (mutable, flexible)

marks = [95, 98, 97, "math"]
print(marks)         # prints whole list
print(marks[0])      # access element by index

# Adding items
marks.append(99)
print(marks)

# Insert item at specific position
marks.insert(2, 88)
print(marks)

# Length of list
print(len(marks))

# Looping through list
print("Loop using for:")
for score in marks:
    print(score)

print("Loop using while:")
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# Break & Continue examples
print("Continue example:")
for x in range(1, 21):
    if x == 15:
        continue  # skips 15
    print(x)

print("Break example:")
for x in range(1, 21):
    if x == 15:
        break  # stops loop at 15
    print(x)
