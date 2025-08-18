# 🌀 Type Conversion in Python

## 🔹 Why we need it?
- The `input()` function **always returns a string**, even if you type a number.
- Example:
  ```python
  age = input("Enter your age: ")   # user enters 21
  print(age + 2)   # ❌ Error! because "21" is a string
