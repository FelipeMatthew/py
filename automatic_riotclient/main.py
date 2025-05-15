import json
import time
import subprocess
import pyautogui
import os

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

VALORANT_PATH = r"C:\Riot Games\Riot Client\RiotClientServices.exe"

# Coordenadas

# AJUSTAR COORDENADAS CONFORME JANELAS ABERTAS / TAMANHO DA TELA 
NAVBAR_COORDS = (462, 1065)  
USERNAME_COORDS = (279, 372)
INSIDE_CLIENT_COORDS = (236, 521) 
RUN_VALORANT_COORDS = (466, 413)  

def load_accounts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def display_accounts(accounts):
    print("\nContas disponíveis:")
    for idx, account in enumerate(accounts, 1):
        print(f"{idx}. Name: {account['name']}, Account: {account['account']}")

def select_account(accounts):
    display_accounts(accounts)
    print("\nDigite o número da conta ou o 'name' da conta:")
    choice = input("> ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(accounts):
            return accounts[idx]
        else:
            print("Número inválido!")
            return None

    else:
        for account in accounts:
            if account['name'].lower() == choice.lower():
                return account
        print("Name não encontrado!")
        return None

def open_valorant():
    if os.path.exists(VALORANT_PATH):
        subprocess.Popen([VALORANT_PATH, "--launch-product=valorant"])
        print("Abrindo o cliente do Valorant...")
        time.sleep(12)
    else:
        print("Caminho do Riot Client inválido! Verifique o VALORANT_PATH.")
        exit(1)

def login_valorant(account):
    try:
        print("Clicando no navbar...")
        pyautogui.click(x=NAVBAR_COORDS[0], y=NAVBAR_COORDS[1])
        time.sleep(1)

        print("Clicando no campo de email...")
        pyautogui.click(x=USERNAME_COORDS[0], y=USERNAME_COORDS[1])
        time.sleep(0.3)

        print("Preenchendo campo de email...")
        pyautogui.write(account['account'])
        pyautogui.press('tab')
        time.sleep(0.3)

        print("Preenchendo campo de senha...")
        pyautogui.write(account['password'])

        print("Navegando para o botão de login...")
        for _ in range(7):
            pyautogui.press('tab')
            time.sleep(0.3)

        pyautogui.press('enter')
        print("Login iniciado. Aguarde o cliente processar...")
        time.sleep(10)

        print("Clicando no inside client...")
        pyautogui.click(x=INSIDE_CLIENT_COORDS[0], y=INSIDE_CLIENT_COORDS[1])
        time.sleep(1)
        
        print("Clicando no botão Run Valorant...")
        pyautogui.click(x=RUN_VALORANT_COORDS[0], y=RUN_VALORANT_COORDS[1])
        time.sleep(5)
        print("Valorant iniciado!")

    except Exception as e:
        print(f"Erro durante o processo: {e}")

def main():
    accounts = load_accounts('accounts.json')
    
    selected_account = select_account(accounts)
    if selected_account:
        print(f"\nConta selecionada: {selected_account['name']} ({selected_account['account']})")

        open_valorant()

        login_valorant(selected_account)
    else:
        print("Nenhuma conta selecionada. Encerrando...")

if __name__ == "__main__":
    main()