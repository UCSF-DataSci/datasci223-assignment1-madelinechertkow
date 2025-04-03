#!/usr/bin/env python3
"""
Email Hasher Script

This script takes an email address as a command line argument,
hashes it using the SHA-256 algorithm, and writes the hash to a file.

Usage:
    python email_hasher.py <email_address>

Example:
    python email_hasher.py example@email.com
"""

import sys
import hashlib
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("email", help = "Don't forget to put the email you want to hash!")



def hash_email(email):
    """
    Hash an email address using SHA-256 and return the hexadecimal digest.
    
    Args:
        email (str): The email address to hash
        
    Returns:
        str: The SHA-256 hash of the email in hexadecimal format
    """
    email_hash = hashlib.sha256(email.encode()).hexdigest()
    # TODO: Implement this function
    # 1. Convert the email string to bytes
    # 2. Create a SHA-256 hash of the email
    # 3. Return the hash in hexadecimal format
    return email_hash

def write_hash_to_file(hash_value, filename="hash.email"):
    """
    Write a hash value to a file.
    
    Args:
        hash_value (str): The hash value to write
        filename (str): The name of the file to write to (default: "hash.email")
    """
    with open("hash.email", "w") as file:
        file.write(hash_value)
    file.close()
    # TODO: Implement this function
    # 1. Open the file in write mode
    # 2. Write the hash value to the file
    # 3. Close the file
    

def main():
    """
    Main function to process command line arguments and execute the script.
    """
    try:
        args = parser.parse_args()
        email = args.email
    except SystemExit:
        print("Error: You must enter the email you want to hash after the command!")
        sys.exit(1)
    hash = hash_email(email)
    write_hash_to_file(hash)
    # TODO: Implement this function
    # 1. Check if an email address was provided as a command line argument
    # 2. If not, print an error message and exit with a non-zero status
    # 3. If yes, hash the email address
    # 4. Write the hash to a file named "hash.email"
    

if __name__ == "__main__":
    main()
