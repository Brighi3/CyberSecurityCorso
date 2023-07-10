from flask import Flask, request, render_template
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        text = request.form.get('text')
        encryption_type = request.form.get('encryption_type')

        if encryption_type == 'symmetric':
            encrypted_text = symmetric_encrypt(text)
        elif encryption_type == 'asymmetric':
            encrypted_text = asymmetric_encrypt(text)
        elif encryption_type == 'stream':
            encrypted_text = stream_encrypt(text)
        elif encryption_type == 'hash':
            encrypted_text = hash_encrypt(text)
        else:
            return 'Tipo di crittografia non supportato'

        return render_template('result.html', encrypted_text=encrypted_text)

    return render_template('index2.html')


def symmetric_encrypt(text):
    password = b'mysecretpassword'  # Chiave di crittografia
    salt = b'mysalt'  # Sale per il derivato della chiave
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode('utf-8'))

    return encrypted_text.decode('utf-8')


def asymmetric_encrypt(text):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    encrypted_text = public_key.encrypt(
        text.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return base64.urlsafe_b64encode(encrypted_text).decode('utf-8')


def stream_encrypt(text):
    key = os.urandom(16)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(text.encode('utf-8')) + encryptor.finalize()

    return base64.urlsafe_b64encode(encrypted_text).decode('utf-8')


def hash_encrypt(text):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(text.encode('utf-8'))
    hashed_text = digest.finalize()

    return base64.urlsafe_b64encode(hashed_text).decode('utf-8')


if __name__ == '__main__':
    app.run()
