menu = """


[d] Depositar
[s] Sacar
[e] Extrato

[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo+= valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("OPERAÇÃO FALHOU! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        passou_do_saldo = valor> saldo
        passou_do_limite = valor > limite
        passou_do_saque = numero_saques > LIMITE_SAQUES
        if passou_do_saldo:
            print("OPERAÇÃO FALHOU! Dinheiro insuficiente.")
        elif passou_do_limite:
            print("OPERAÇÃO FALHOU! O valor passou do número limite")
        elif passou_do_saque:
            print("OPERAÇÃO FALHOU! Limite de saques atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        nome = "Extrato"
        print(nome.center(20,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione outra opção.")
