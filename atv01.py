class Tarefa:
    def __init__(self, materia):
        self.materia = materia

    def __str__(self):
        return f"Tarefa: {self.materia}"

class Projeto:
    def __init__(self, titulo):
        self.titulo = titulo
        self.tarefas = []  

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)  

    def listar_tarefas(self):
        if not self.tarefas:
            return "Nenhuma tarefa atribuída a este projeto."
        return "\n".join(str(tarefa) for tarefa in self.tarefas)  

    def __str__(self):
        return f"Projeto: {self.titulo}"


tarefa1 = Tarefa('História')
tarefa2 = Tarefa('Matemática')
tarefa3 = Tarefa('Física')


projeto1 = Projeto('Revolução Industrial')


projeto1.adicionar_tarefa(tarefa1)
projeto1.adicionar_tarefa(tarefa2)
projeto1.adicionar_tarefa(tarefa3)


print(projeto1)
print("Tarefas associadas ao projeto:")
print(projeto1.listar_tarefas())
