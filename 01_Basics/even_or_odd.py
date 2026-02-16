# basics/even_or_odd.py

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# One-liner version (more advanced style)
print(f"{number} is {'EVEN' if number % 2 == 0 else 'ODD'}")