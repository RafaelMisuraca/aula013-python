class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_matricula(self):
        return self.__matricula
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
    

aluno1 = Aluno("João", 20, "12345")


print("Nome:", aluno1.get_nome())
print("Idade:", aluno1.get_idade())
print("Matrícula:", aluno1.get_matricula())


aluno1.set_nome("Maria")
aluno1.set_idade(22)
aluno1.set_matricula("54321")


print("Nome atualizado:", aluno1.get_nome())
print("Idade atualizada:", aluno1.get_idade())
print("Matrícula atualizada:", aluno1.get_matricula())