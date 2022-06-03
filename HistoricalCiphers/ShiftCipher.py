# ------- shift ciphers ----------- #

def encrypt(content: str, key: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    lower_content = content.lower()
    encrypted_content = ''
    for letter in lower_content:
        encrypted_content += letters[(letters.index(letter) + key) % len(letters)]

    return encrypted_content


def decrypt(cipher_text: str, key: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_content = ''
    for letter in cipher_text:
        decrypted_content += letters[(letters.index(letter) - key) % len(letters)]

    return decrypted_content
