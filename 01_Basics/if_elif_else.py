# basics/if_elif_else.py

score = int(input("Enter your exam score (0–100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Bonus: pass/fail message
if score >= 50:
    print("Congratulations! You passed! 🎉🎉🎉")
else:
    print("Better luck next time. Keep practicing! 💪💪💪")