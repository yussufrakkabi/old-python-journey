#math_operations.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b:.2f}")     # 2 decimal places
print(f"{a} // {b} = {a // b}")       # integer division
print(f"{a} % {b} = {a % b}")         # remainder
print(f"{a} ** {b} = {a ** b:.2f}")   # power