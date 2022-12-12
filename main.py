"""
A Simple program to encrypt text using RSA encryption.
I am going to follow the steps listed in Wikipedia's article on RSA encryption.
For more details, visit: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""

from RSA_class import RSA_entity


def main():

    print("generating keys...")
    Bob = RSA_entity()
    Alice = RSA_entity()

    N, e = Alice.broadcast_public_key()

    msg = input("Hello Bob, What message would you like to send to Alice? ")
    enc = Bob.encrypt(msg, e, N)

    dec = Alice.decrypt(enc)

    print(f"\nMessage: {msg}\nEncrypted: {enc}\nDecrypted: {dec}\n")


if __name__ == "__main__":
    main()
