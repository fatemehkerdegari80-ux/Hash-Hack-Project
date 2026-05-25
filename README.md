# SHA-256 Password Cracker

A Python script to recover 4-digit passwords from SHA-256 hashes.

## How it works:
- Reads a CSV file with `name,sha256_hash`.
- Tries all numbers from 1000 to 9999.
- Finds the matching password for each hash.
- Writes `name,password` to an output CSV file.

## To Run:
1. Save the script as `source.py`.
2. Have an `input.csv` file in the same folder.
3. Run: `python main.py`
4. Check `output.csv` for results.

**Note:** This script only checks passwords from 1000 to 9999.
