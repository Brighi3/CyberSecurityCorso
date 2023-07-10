from cryptography.fernet import Fernet

# Generazione di una chiave casuale
def genera_chiave():
    return Fernet.generate_key()

# Cifratura del testo in chiaro
def cifra(testo_chiaro, chiave):
    f = Fernet(chiave)
    testo_cifrato = f.encrypt(testo_chiaro.encode())
    return testo_cifrato

# Decifratura del testo cifrato
def decifra(testo_cifrato, chiave):
    f = Fernet(chiave)
    testo_chiaro = f.decrypt(testo_cifrato)
    return testo_chiaro.decode()

# Esempio di utilizzo
chiave_segreta = genera_chiave()
testo_originale = "Questo è un messaggio di pubblico dominio."

testo_cifrato = cifra(testo_originale, chiave_segreta)
print("Testo cifrato:", testo_cifrato)

testo_decifrato = decifra(testo_cifrato, chiave_segreta)
print("Testo decifrato:", testo_decifrato)
