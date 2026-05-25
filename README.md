# 🔐 Password Hash Cracker (SHA-256)

A simple Python script that attempts to **recover numeric passwords** from their SHA-256 hashes using a **brute-force dictionary attack**.

---

## 🚀 Overview

This project reads a CSV file containing usernames and hashed passwords, and attempts to recover the original passwords by:

1. Generating all **4-digit numeric passwords (1000–9999)**
2. Hashing each using SHA-256
3. Matching them against the hashes in the input file

If a match is found, the original password is written to an output CSV file.

---

## 🧠 How It Works

- Uses Python's built-in `hashlib` library
- Precomputes hashes for all 4-digit numbers
- Stores them in a dictionary for fast lookup
- Compares each input hash against generated hashes

---

## 📁 Input Format

The input file (`input.csv`) must be structured as:

```
username,hashed_password
```

### Example:

```
alice,5e884898da28047151d0e56f8dc6292773603d0d6aabbdd...
bob,03ac674216f3e15c761ee1a5e255f067953623c8b388b445...
```

---

## 📤 Output Format

The output file (`output.csv`) will contain:

```
username,password
```

### Example:

```
alice,1234
bob,5678
```

---

## ⚙️ Usage

### Run the script:

```bash
python script.py
```

The script will:

- Read from `input.csv`
- Write results to `output.csv`

---

## 🧩 Code Structure

### Main Function

```python
hash_password_hack(input_file_name, output_file_name)
```

### Steps:

1. Generate SHA-256 hashes for numbers 1000–9999
2. Store them in a dictionary (`hash → number`)
3. Read input CSV
4. Match hashes
5. Write results to output CSV

---

## 📌 Notes

- Only works for **4-digit numeric passwords**
- Uses brute-force → not efficient for large spaces
- SHA-256 is a one-way function, so guessing is required
- Uses `OrderedDict` to preserve insertion order

---

## 💡 Applications

- Educational demonstration of hashing
- Understanding brute-force attacks
- Security awareness training
