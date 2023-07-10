from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.ciphers import modes

# Cifratura del testo in chiaro
def cifra(testo_chiaro, chiave, nonce):
    cifratore = Cipher(algorithms.Salsa20(chiave), mode=modes.Salsa20(nonce))
    cifratore = cifratore.encryptor()
    testo_cifrato = cifratore.update(testo_chiaro) + cifratore.finalize()
    return testo_cifrato

# Decifratura del testo cifrato
def decifra(testo_cifrato, chiave, nonce):
    decifratore = Cipher(algorithms.Salsa20(chiave), mode=modes.Salsa20(nonce))
    decifratore = decifratore.decryptor()
    testo_chiaro = decifratore.update(testo_cifrato) + decifratore.finalize()
    return testo_chiaro

# Esempio di utilizzo
chiave_segreta = b'UnaChiaveSegreta'  # Chiave di cifratura
nonce = b'UnNonceCasuale'  # Nonce casuale
testo_originale = b'Questo è un messaggio segreto.'

testo_cifrato = cifra(testo_originale, chiave_segreta, nonce)
print("Testo cifrato:", testo_cifrato)

testo_decifrato = decifra(testo_cifrato, chiave_segreta, nonce)
print("Testo decifrato:", testo_decifrato)