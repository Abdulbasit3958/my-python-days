# Type Conversion Examples

# Example 1
# old_age = input("what is your age? :")
# new_age = old_age + 2
# print(new_age)

old_age = input("What is your age? : ")
new_age = int(old_age) + 2
print(new_age)

print("--------------------------------------------------")

# Example 2
number = 18
print(number)
print(float(number))
print(str(number))
print(bool(number))

print("--------------------------------------------------")

# Example 3
first = input("Enter first number: ")
second = input("Enter second number: ")
sum_wrong = first + second
print(sum_wrong)

print("--------------------------------------------------")

# Example 4
first = input("Enter first number again: ")
second = input("Enter second number again: ")
sum_correct = int(first) + int(second)
print(sum_correct)

print("--------------------------------------------------")

# Example 5
first = input("Enter first number one more time: ")
second = input("Enter second number one more time: ")
sum_final = int(first) + int(second)
print("Your value is: " + str(sum_final))
