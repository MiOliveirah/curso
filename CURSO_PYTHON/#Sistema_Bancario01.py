#Sistema_Bancario

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    print("\n========== MENU ==========")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. O depósito deve ser positivo.")

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))
        if valor > limite_saque:
            print("Valor do saque excede o limite permitido por saque.")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "0":
        print("Saindo... Obrigado por utilizar nosso sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")
