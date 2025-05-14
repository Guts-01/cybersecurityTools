#!/bin/bash

echo "[*] Instalando ferramenta whatpwd..."

# Pasta de destino
DEST="/opt/whatpwd"

# Criar pasta se não existir
sudo mkdir -p $DEST

# Copiar arquivos
sudo cp whatpwd.py wordgen.py $DEST

# Garantir permissões
sudo chmod +x $DEST/whatpwd.py

# Criar link simbólico em /usr/local/bin
echo "[*] Criando atalho global em /usr/local/bin/whatpwd..."
sudo ln -sf $DEST/whatpwd.py /usr/local/bin/whatpwd

# Instalar dependência requests
echo "[*] Verificando se 'requests' está instalado..."
if ! pip show requests &>/dev/null; then
    echo "[*] Instalando 'requests' com pip..."
    pip install requests
else
    echo "[+] 'requests' já está instalado."
fi

echo "[+] Instalação concluída. Use o comando 'whatpwd' no terminal!"
