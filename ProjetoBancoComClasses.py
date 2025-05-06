import textwrap

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(Deposito(valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif self.numero_saques >= self.limite_saques:
            print("Número máximo de saques atingido.")
        else:
            self.saldo -= valor
            self.transacoes.append(Saque(valor))
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n==================== Extrato ====================")
        if not self.transacoes:
            print("Nenhuma movimentação realizada.")
        else:
            for t in self.transacoes:
                print(t)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Saques realizados: {self.numero_saques}")

class Transacao:
    def __init__(self, valor):
        self.valor = valor

class Saque(Transacao):
    def __str__(self):
        return f"Saque: R$ {self.valor:.2f}"

class Deposito(Transacao):
    def __str__(self):
        return f"Depósito: R$ {self.valor:.2f}"

def menu():
    menu = """
    ------------------------------------------------
    **************************************************
            Bem-vindo ao Banco QUEBRADO!
    **************************************************
            Operações disponíveis:

    A. Depositar
    B. Sacar
    C. Extrato
    D. Cadastrar Cliente
    E. Criar Conta
    F. Listar Contas
    G. Para Sair
    -------------------------------------------------
    """
    return input(textwrap.dedent(menu))

def encontrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def main():
    clientes = []
    contas = []
    agencia_padrao = "0001"

    while True:
        opcao = menu().strip().upper()

        if opcao == "A":
            cpf = input("CPF do titular: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "B":
            cpf = input("CPF do titular: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "C":
            cpf = input("CPF do titular: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente and cliente.contas:
                conta = cliente.contas[0]
                conta.exibir_extrato()
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "D":
            cpf = input("CPF: ")
            if encontrar_cliente(cpf, clientes):
                print("Cliente já cadastrado.")
                continue
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereço: ")
            clientes.append(Cliente(nome, cpf, data_nascimento, endereco))
            print("Cliente cadastrado com sucesso!")

        elif opcao == "E":
            cpf = input("CPF do titular: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente:
                numero_conta = len(contas) + 1
                conta = Conta(agencia_padrao, numero_conta, cliente)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print("Conta criada com sucesso!")
            else:
                print("Cliente não encontrado.")

        elif opcao == "F":
            for conta in contas:
                print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {conta.cliente.nome}")

        elif opcao == "G":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
