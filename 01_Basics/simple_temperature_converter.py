# basics/simple_temperature_converter.py

print("1 → Celsius to Fahrenheit")
print("2 → Fahrenheit to Celsius")
choice = input("Choose conversion (1 or 2): ")

temp = float(input("Enter temperature: "))

if choice == "1":
    f = (temp * 9/5) + 32
    print(f"{temp}°C = {f:.1f}°F")
elif choice == "2":
    c = (temp - 32) * 5/9
    print(f"{temp}°F = {c:.1f}°C")
else:
    print("Invalid choice!")