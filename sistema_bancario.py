import textwrap

def menu():
    menu = """\n    
    MENUS
    [d]\tDeposit
    [s]\Saquo
    [e]\tExtratos
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNew User
    [q]\tQuit
    
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    
    else:
        print("Valor inválido. Por favor, digite um valor positivo.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuário já cadastrado!")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    endereco = input("Informe o endereco do usuário: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuarios in usuarios if usuario[cpf] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor a depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

            

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(saldo, valor, extrato)


        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
                