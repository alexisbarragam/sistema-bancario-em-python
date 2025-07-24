# Sistema Bancário em Python
# Autor: Alexis Barragam
# Este programa simula operações básicas de um banco: depósito, saque e extrato.

# === Constantes do sistema ===
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIO = 3


def exibir_menu():
    print("""
================ MENU ================
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
======================================
""")

def depositar(saldo):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        print("❌ Valor inválido. Tente novamente.")
        return saldo, None
    if valor > 0:
        saldo += valor
        print("✅ Depósito realizado com sucesso!")
        return saldo, ("Depósito", valor)
    else:
        print("❌ Operação falhou! O valor informado é inválido.")
        return saldo, None

def sacar(saldo, numero_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        print("❌ Valor inválido. Tente novamente.")
        return saldo, numero_saques, None
    if valor <= 0:
        print("❌ Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("❌ Operação falhou! Saldo insuficiente.")
    elif valor > LIMITE_SAQUE:
        print(f"❌ Operação falhou! Limite máximo por saque: R$ {LIMITE_SAQUE:.2f}.")
    elif numero_saques >= LIMITE_SAQUES_DIARIO:
        print("❌ Operação falhou! Limite diário de saques atingido.")
    else:
        saldo -= valor
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
        return saldo, numero_saques, ("Saque", valor)
    return saldo, numero_saques, None

def exibir_extrato(saldo, logs):
    print("\n================ EXTRATO ================")
    if not logs:
        print("Nenhuma movimentação realizada.")
    else:
        for tipo, valor in logs:
            print(f"{tipo}:\tR$ {valor:.2f}")
    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("==========================================\n")

def main():
    saldo = 0
    numero_saques = 0
    logs = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            saldo, log = depositar(saldo)
            if log:
                logs.append(log)
        elif opcao == "2":
            saldo, numero_saques, log = sacar(saldo, numero_saques)
            if log:
                logs.append(log)
        elif opcao == "3":
            exibir_extrato(saldo, logs)
        elif opcao == "0":
            print("\n👋 Obrigado por usar nosso banco. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()