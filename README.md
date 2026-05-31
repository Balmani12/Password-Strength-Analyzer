# 🔐 Advanced Password Strength Analyzer

A Python-based security tool that evaluates password strength, estimates crack time, detects password reuse, and suggests stronger alternatives using cryptographic techniques.

---

## 📌 About

This tool was built to demonstrate real-world password security concepts including entropy calculation, hash-based reuse detection, and brute-force resistance estimation — key concepts in cybersecurity and secure application development.

---

## ✨ Features

- ✅ **Password Strength Rating** — Weak / Medium / Strong
- ✅ **Entropy Calculation** — Measures randomness in bits
- ✅ **Crack Time Estimation** — Estimates time to brute force
- ✅ **Password Reuse Detection** — Uses SQLite + SHA256 hashing
- ✅ **Common Password Detection** — Flags weak common passwords
- ✅ **Complexity Analysis** — Checks uppercase, lowercase, digits, special characters
- ✅ **Strong Password Generator** — Suggests 3 secure random passwords
- ✅ **Security Feedback** — Provides improvement suggestions

---

## 🛠️ Technologies Used

- Python 3
- SQLite3 (password history database)
- Hashlib (SHA256 password hashing)
- Regex (pattern matching)
- Math (entropy calculation)
- Random + String (password generation)

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Balmani12/password-strength-analyzer

# Navigate to folder
cd password-strength-analyzer

# Run the tool
python Password_Strength_Analyzer.py
```

---

## 📊 Sample Output

```
=======================================================
        ADVANCED PASSWORD STRENGTH ANALYZER
=======================================================

Enter your password: MyP@ssw0rd123

=======================================================
PASSWORD SECURITY REPORT
=======================================================

Password Strength    : STRONG
Password Length      : 13 characters
Password Entropy     : 77.63 bits
Estimated Crack Time : 3074 years

Excellent password security practices detected.

[+] Password hash securely stored in database.
```

---

## 🔐 Security Concepts Covered

- **Password Entropy** — Measures unpredictability of a password
- **SHA256 Hashing** — Secure one-way password storage
- **Brute Force Resistance** — Time estimation based on entropy
- **Password Reuse Prevention** — Database-backed hash comparison
- **OWASP Password Guidelines** — Length, complexity, uniqueness

---

## 📚 What I Learned

- Cryptographic hashing with SHA256
- Password entropy and brute force mathematics
- Secure password storage using hashing (never plaintext)
- SQLite database integration in Python
- Real-world password security best practices

---

## 👨‍💻 Author

**Balmani**
- 🔗 LinkedIn: [linkedin.com/in/bal-mani-7457a11ba](https://linkedin.com/in/bal-mani-7457a11ba)
- 🐙 GitHub: [github.com/Balmani12](https://github.com/Balmani12)
- 🎯 TryHackMe: [tryhackme.com/p/balmani](https://tryhackme.com/p/balmani)
