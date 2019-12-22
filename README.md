# Hash and Hash-Cracking

Simple Python code to demonstrate Hashing for Google Code-In 2019

## How to run

```bash
git clone https://github.com/Wooniety/Hashing-and-Hash-Cracking
cd Hashing-and-Hash-Cracking
python main.py
```

## Hashing types

- md5
- sha1
- sha224
- sha256
- sha384
- sha512

## What it does

### Hashing

#### Single string

Enter string and pick hash type, hashed string will be printed.

#### A wordlist

Keep file in the same folder, then enter filename of wordlist when prompted. The hashed result will go to `output.txt`
> Note: Ensure words are seperated by **newline only**

### Hash-Cracking

Enter hashed string and hash type, it will search the hash list in `dictionary/name_of_hash.csv` for a matching string. If found, it will print out the word.
