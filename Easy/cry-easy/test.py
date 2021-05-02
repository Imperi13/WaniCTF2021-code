with open("output.txt") as f:
    enc = f.read().strip()


plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

assert all(x in plaintext_space for x in enc)


def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

def decrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (x-b)*pow(5,-1,26) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext


if __name__ == "__main__":
    ciphertext = decrypt(enc, a=5, b=8)
    print(ciphertext)
