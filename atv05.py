class ContaBancaria:
    def __init__(self, numero_conta, saldo=0):
        self.__numero_conta = numero_conta
        self.__saldo = saldo
        self.__transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.__transacoes.append(f"Saque: -{valor}")
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.__saldo}")
        elif valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser positivo.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

    def extrato(self):
        print("\n--- Extrato de Transações ---")
        for transacao in self.__transacoes:
            print(transacao)
        print(f"Saldo final: R${self.__saldo}\n")


conta = ContaBancaria(numero_conta="12345")


conta.depositar(100)
conta.depositar(50)


conta.sacar(30)
conta.sacar(200)  

# Verificando o saldo
conta.verificar_saldo()


conta.extrato()