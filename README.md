# Sistema Bancário Otimizado com Funções

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Sobre o Projeto

Este projeto representa a evolução de um sistema bancário simples, desenvolvido em Python. Inicialmente criado como um script procedural, foi **refatorado para utilizar uma estrutura modular com funções**, aplicando conceitos mais avançados de programação.

Esta otimização foi realizada como parte do segundo desafio de projeto do Bootcamp Santander DIO - Back-End com Python, focando em criar um código mais limpo, legível e de fácil manutenção.

## Funcionalidades

O sistema permite realizar as seguintes operações bancárias via terminal:

-   **Depositar:** Adicionar valores positivos ao saldo da conta.
-   **Sacar:** Retirar valores da conta, respeitando as seguintes regras:
    -   Limite de **3 saques** diários.
    -   Valor máximo de **R$ 500,00** por saque.
    -   Não permite saque se o saldo for insuficiente.
-   **Exibir Extrato:** Listar todos os depósitos e saques realizados, além do saldo atual da conta.

## Programas e Conceitos Aplicados

A versão atual do projeto foi desenvolvida utilizando Python e aplica os seguintes conceitos:

-   **Funções:** O código foi modularizado em funções para cada operação (`sacar`, `depositar`, `exibir_extrato`, `menu`).
-   **Argumentos Posicionais e Nomeados:** Uso das sintaxes especiais `*` (keyword-only) e `/` (positional-only) para maior clareza e robustez na chamada das funções.
-   **Estruturas de Controle:** Utilização de `while` para o loop principal do programa e `if/elif/else` para a lógica das operações.
-   **Manipulação de Estado:** Passagem de estado (saldo, extrato, etc.) como argumentos e retornos de funções, evitando o uso de variáveis globais.
-   **Uso de Constantes:** Para valores fixos como o limite de saques, melhorando a legibilidade.
-   **Manipulação de Strings:** Uso de f-strings para formatação de saídas e do extrato.
-   **Versionamento de Código:** Utilização de Git e GitHub para controle de versão e documentação.

## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/alexisbarragam/sistema-bancario-em-python.git](https://github.com/alexisbarragam/sistema-bancario-em-python.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd sistema-bancario-em-python
    ```
3.  **Execute o script Python:**
    ```bash
    python sistema-bancario.py
    ```

## Histórico de Alterações

### v2.0 - Refatoração com Funções (Atual)
- **Modularização completa do código:** As operações de saque, depósito e extrato foram isoladas em suas próprias funções.
- **Eliminação de variáveis globais:** O estado da aplicação (`saldo`, `extrato`, etc.) agora é controlado e passado através de parâmetros e retornos de função.
- **Adoção de boas práticas:** Implementação de uma função `main()` para orquestrar o programa, uso de constantes e assinatura de funções com argumentos posicionais e nomeados.
- **Melhora significativa na legibilidade e manutenção** do código.

### v1.0 - Versão Inicial
- Implementação das funcionalidades básicas (depósito, saque com limites, extrato).
- Estrutura de código procedural em um único script.
- Lógica de controle implementada com `if/elif/else` dentro de um loop principal.