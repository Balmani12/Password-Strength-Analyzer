import re
import math
import random
import string
import hashlib
import sqlite3
from datetime import datetime

# ==========================================
# DATABASE SETUP
# ==========================================

conn = sqlite3.connect("password_history.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS password_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash TEXT UNIQUE,
    created_at TEXT
)
""")

conn.commit()

# ==========================================
# COMMON WEAK PASSWORDS
# ==========================================

COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "abc123",
    "password123"
]

# ==========================================
# HASH PASSWORD
# ==========================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ==========================================
# CHECK PASSWORD REUSE
# ==========================================

def is_password_reused(password):
    hashed = hash_password(password)

    cursor.execute(
        "SELECT * FROM password_history WHERE password_hash=?",
        (hashed,)
    )

    return cursor.fetchone() is not None

# ==========================================
# SAVE PASSWORD HASH
# ==========================================

def save_password(password):
    hashed = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO password_history(password_hash, created_at) VALUES(?, ?)",
            (hashed, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()

    except sqlite3.IntegrityError:
        pass

# ==========================================
# PASSWORD ENTROPY
# ==========================================

def calculate_entropy(password):

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"[0-9]", password):
        charset_size += 10

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/|\\]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)

    return round(entropy, 2)

# ==========================================
# ESTIMATE CRACK TIME
# ==========================================

def estimate_crack_time(entropy):

    guesses_per_second = 1e9

    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{round(seconds)} seconds"

    elif seconds < 3600:
        return f"{round(seconds / 60)} minutes"

    elif seconds < 86400:
        return f"{round(seconds / 3600)} hours"

    elif seconds < 31536000:
        return f"{round(seconds / 86400)} days"

    else:
        return f"{round(seconds / 31536000)} years"

# ==========================================
# PASSWORD STRENGTH CHECKER
# ==========================================

def check_password_strength(password):

    score = 0
    feedback = []

    # -------------------------
    # Length Check
    # -------------------------
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        feedback.append("Password should be at least 8 characters long.")

    # -------------------------
    # Complexity Checks
    # -------------------------
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/|\\]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # -------------------------
    # Common Password Check
    # -------------------------
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a very common password.")
        score = max(score - 2, 0)

    # -------------------------
    # Repeated Characters
    # -------------------------
    if re.search(r"(.)\1\1", password):
        feedback.append("Avoid repeated characters.")

    # -------------------------
    # Entropy
    # -------------------------
    entropy = calculate_entropy(password)

    # -------------------------
    # Strength Rating
    # -------------------------
    if score <= 2:
        strength = "WEAK"

    elif score <= 5:
        strength = "MEDIUM"

    else:
        strength = "STRONG"

    return strength, feedback, entropy

# ==========================================
# STRONG PASSWORD GENERATOR
# ==========================================

def generate_strong_password(length=16):

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+")

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            "!@#$%^&*()_+"
        )
        for _ in range(length - 4)
    )

    password_list = list(lowercase + uppercase + digit + special + remaining)

    random.shuffle(password_list)

    return ''.join(password_list)

# ==========================================
# MAIN PROGRAM
# ==========================================

print("=" * 55)
print("        ADVANCED PASSWORD STRENGTH ANALYZER")
print("=" * 55)

password = input("\nEnter your password: ")

# ------------------------------------------
# Reuse Check
# ------------------------------------------

if is_password_reused(password):

    print("\n[!] WARNING: Password has already been used before.")
    print("    Please use a unique password.\n")

else:

    strength, feedback, entropy = check_password_strength(password)

    print("\n" + "=" * 55)
    print("PASSWORD SECURITY REPORT")
    print("=" * 55)

    print(f"\nPassword Strength : {strength}")
    print(f"Password Length   : {len(password)} characters")
    print(f"Password Entropy  : {entropy} bits")

    crack_time = estimate_crack_time(entropy)

    print(f"Estimated Crack Time : {crack_time}")

    # --------------------------------------
    # Feedback
    # --------------------------------------

    if feedback:

        print("\nSecurity Suggestions:")

        for item in feedback:
            print(f" - {item}")

    else:
        print("\nExcellent password security practices detected.")

    # --------------------------------------
    # Suggest Strong Password
    # --------------------------------------

    if strength != "STRONG":

        print("\nSuggested Strong Passwords:")

        for i in range(3):
            print(f" {i+1}. {generate_strong_password()}")

    # --------------------------------------
    # Save Password Hash
    # --------------------------------------

    save_password(password)

    print("\n[+] Password hash securely stored in database.")

print("\nProgram Finished.")
print("=" * 55)

# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()