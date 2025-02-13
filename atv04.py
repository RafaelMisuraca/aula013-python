class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco) :
        if novo_preco < 0:
            print("Não é possível ter preço negativo.")
        else:
            self.__preco = novo_preco
    
    def set_quantidade(self, nova_quantidade):
        if nova_quantidade < 0:
            print("Não é possível ter quantidade negativa")
        else:
            self.__quantidade = nova_quantidade
    
produto1 = Produto("Pão", 6, 20)

print("Nome:", produto1.get_nome())
print('Preco:', produto1.get_preco())
print('Quantidade em Estoque:', produto1.get_quantidade())

produto1.set_nome('Maçã')
produto1.set_preco(8)
produto1.set_quantidade(40)

print("Nome Atualizado:", produto1.get_nome())
print('Preco Atualizado:', produto1.get_preco())
print('Quantidade em Estoque Atualizado:', produto1.get_quantidade())
