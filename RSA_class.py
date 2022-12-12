from helpers import generate_prime, compute_totient, choose_e, determine_d


class RSA_entity():
    def __init__(self):
        # keep secret
        self.p = generate_prime(1024)
        # keep secret
        self.q = generate_prime(1024)

        self.n = self.p * self.q  # to be released as part of public key

        # keep secret
        self.totient = compute_totient(self.p, self.q)

        self.e = choose_e(self.totient)  # released as part of public key

        # keep secret
        self.d = determine_d(self.e, self.totient)

    def encrypt(self, message, e, N):
        # Convert the message to integer, pad it and then encrypt it
        # Padding scheme: space between parts

        ciphertext = ""
        for character in message:
            ciphertext += str(pow(ord(character), e, N)) + " "
        return ciphertext

    def decrypt(self, ciphertext):

        message = ""
        # Reverse the padding scheme
        # Padding scheme: space between parts
        splitted = ciphertext.split()
        for each in splitted:
            if each:
                message += chr(pow(int(each), self.d, self.n))
        return message

    def broadcast_public_key(self):
        return self.n, self.e
