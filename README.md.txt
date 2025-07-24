Sistema Bancário em Python


Este é um projeto simples que simula operações bancárias básicas usando Python. Ideal para praticar lógica, estrutura de código e controle de fluxo.

> Este projeto foi desenvolvido por Alexis Barragam. 

      (https://github.com/alexisbarragam)



Funcionalidades;

- Depósito (aceita apenas valores positivos)
- Saque (com limite de R$500 por operação e até 3 saques por dia)
- Extrato com histórico de transações e saldo atual
- Interface via terminal (CLI), com mensagens amigáveis



Sobre o código;

O sistema foi desenvolvido com funções bem definidas, separando responsabilidades de forma clara:

- `depositar()` → valida, registra e retorna o depósito
- `sacar()` → aplica regras de negócio e retorna saque (ou erros amigáveis)
- `exibir_extrato()` → mostra todo o histórico da conta, formatado
- `main()` → organiza o menu e orquestra o funcionamento geral

O histórico de movimentações é armazenado como uma lista de tuplas:
```python
logs = [("Depósito", 150.00), ("Saque", 80.00)]
