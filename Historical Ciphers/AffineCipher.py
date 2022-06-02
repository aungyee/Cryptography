# -------- Affine Ciphers --------- #
import math
import random


def generate_a(mod: int):
    while True:
        a = random.randint(0, 10000)
        if math.gcd(a, mod) == 1:
            return a


def get_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i


def encrypt(content: str, a: int, b: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    lower_content = content.lower()
    encrypted_content = ''
    for letter in lower_content:
        encrypted_content += letters[(a * letters.index(letter) + b) % len(letters)]

    return encrypted_content


def decrypt(cipher_text: str, a: int, b: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_content = ''
    for letter in cipher_text:
        decrypted_content += letters[((letters.index(letter) - b) * get_inverse(a)) % len(letters)]

    return decrypted_content


if __name__ == '__main__':
    A = generate_a(26)
    print(encrypt('attack', A, 12))
    print(decrypt(encrypt('attack', A, 12), A, 12))
