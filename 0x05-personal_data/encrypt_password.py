#!/usr/bin/env python3
"""
Implement a hash_password function that expects one string
argument name password and returns a salted, hashed password,
which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw)
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Take in a password to hash and return a salted
    byte string.
    """
    password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
