# Sistema Bancário em Python
# Autor: Alexis Barragam
# Este programa simula operações básicas de um banco: depósito, saque e extrato.

# === Constantes do sistema ===
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIO = 3


def exibir_menu():
    print("""
╔════════════════ MENU ════════════════╗
║ [1] Depositar                       ║
║ [2] Sacar                           ║
║ [3] Extrato                         ║
║ [0] Sair                            ║
╚══════════════════════════════════════╝
""")

def mensagem_sucesso(msg):
    print(f"\n╔══════════════════════════════════════╗")
    print(f"║ SUCESSO: {msg:<30}║")
    print(f"╚══════════════════════════════════════╝\n")

def mensagem_erro(msg):
    print(f"\n╔══════════════════════════════════════╗")
    print(f"║ ERRO: {msg:<33}║")
    print(f"╚══════════════════════════════════════╝\n")

def depositar(saldo):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
    except ValueError:
        mensagem_erro("Valor inválido. Tente novamente.")
        return saldo, None
    if valor > 0:
        saldo += valor
        mensagem_sucesso("Depósito realizado com sucesso!")
        return saldo, ("Depósito", valor)
    else:
        mensagem_erro("Operação falhou! O valor informado é inválido.")
        return saldo, None

def sacar(saldo, numero_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))
    except ValueError:
        mensagem_erro("Valor inválido. Tente novamente.")
        return saldo, numero_saques, None
    if valor <= 0:
        mensagem_erro("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        mensagem_erro("Operação falhou! Saldo insuficiente.")
    elif valor > LIMITE_SAQUE:
        mensagem_erro(f"Operação falhou! Limite máximo por saque: R$ {LIMITE_SAQUE:.2f}.")
    elif numero_saques >= LIMITE_SAQUES_DIARIO:
        mensagem_erro("Operação falhou! Limite diário de saques atingido.")
    else:
        saldo -= valor
        numero_saques += 1
        mensagem_sucesso("Saque realizado com sucesso!")
        return saldo, numero_saques, ("Saque", valor)
    return saldo, numero_saques, None

def exibir_extrato(saldo, logs):
    print("\n╔════════════════ EXTRATO ═════════════╗")
    if not logs:
        print("║ Nenhuma movimentação realizada.     ║")
    else:
        for tipo, valor in logs:
            print(f"║ {tipo:<10} \tR$ {valor:>10.2f}           ║")
    print(f"║                                    ║")
    print(f"║ Saldo atual: \tR$ {saldo:>10.2f}           ║")
    print("╚══════════════════════════════════════╝\n")

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
            print("\n======================================")
            print("Obrigado por usar nosso banco. Até logo!")
            print("======================================\n")
            break
        else:
            mensagem_erro("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()