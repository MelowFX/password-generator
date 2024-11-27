"""Password generator module."""

import string
from random import choice, randint

LENGTH = 10


def generate():
    """
    Generate a random password.

    Returns:
        str: A random password of LENGTH containing letters and digits.
    """
    password = ""

    for _ in range(LENGTH):
        char = choice(string.ascii_letters + string.digits + string.punctuation)

        if randint(0, 1) == 1:
            char = char.upper()

        password += char

    return password


if __name__ == "__main__":
    result = generate()
    print(result)
