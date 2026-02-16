# String Manipulation
def string_demo():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(f"Word: {w:15} Length: {len(w)}")

# Math and Logic
def math_logic():
    # Countdown / Unit conversion
    usr_in_seconds = 3665
    hours = usr_in_seconds // 3600
    minutes = (usr_in_seconds % 3600) // 60
    seconds = usr_in_seconds % 60
    print(f"Time: {hours}h {minutes}m {seconds}s")

# Factorial logic (Fixed your original code)
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    string_demo()
    print(f"Factorial of 5: {calculate_factorial(5)}")