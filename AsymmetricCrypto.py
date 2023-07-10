from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generazione di una coppia di chiavi RSA
def genera_chiavi():
    chiave_privata = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    chiave_pubblica = chiave_privata.public_key()
    return chiave_privata, chiave_pubblica

# Cifratura del testo in chiaro utilizzando la chiave pubblica
def cifra(testo_chiaro, chiave_pubblica):
    testo_chiaro = testo_chiaro.encode()
    testo_cifrato = chiave_pubblica.encrypt(
        testo_chiaro,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return testo_cifrato

# Decifratura del testo cifrato utilizzando la chiave privata
def decifra(testo_cifrato, chiave_privata):
    testo_chiaro = chiave_privata.decrypt(
        testo_cifrato,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return testo_chiaro.decode()

# Esempio di utilizzo
chiave_privata, chiave_pubblica = genera_chiavi()
testo_originale = "AB"

testo_cifrato = cifra(testo_originale, chiave_pubblica)
print("Testo cifrato:", testo_cifrato)

testo_decifrato = decifra(testo_cifrato, chiave_privata)
print("Testo decifrato:", testo_decifrato)
