import hashlib

# Calcolo dell'hash SHA-1 di una stringa
def calcola_hash(testo):
    sha1_hash = hashlib.sha1(testo.encode()).hexdigest()
    return sha1_hash

# Esempio di utilizzo
testo_originale = "Questo è un messaggio da crittografare."

hash_sha1 = calcola_hash(testo_originale)
print("Hash SHA-1:", hash_sha1)