import re

password = input("Enter your password: ")
score = 0

# Checks
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should be at least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter")

if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter")

if re.search(r"[0-9]", password):
    score += 1
else:
    print("❌ Add at least one number")

if re.search(r"[!@#$%^&*]", password):
    score += 1
else:
    print("❌ Add at least one special character")

# Final result
if score <= 2:
    print("🔴 Weak Password")
elif score <= 4:
    print("🟡 Medium Password")
else:
    print("🟢 Strong Password")
if score <= 2:
    print("Suggestion: Use mix of uppercase, lowercase, numbers & symbols")
elif score == 3 or score == 4:
    print("Suggestion: Add more complexity to make it stronger")