
# Gerenciador de tarefas + calendario
"""
    Implementar interface grafica utilizando o pyQt e implementar 
    sistema de calendario / alarme ao codigo
"""

# classe para representar as tarefas
class Tarefa:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data

# classe para representar a lista de tarefas


class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    # método para adicionar uma nova tarefa
    def adcionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    # método para excluir uma tarefa
    def excluir_tarefa(self, indice):
        self.tarefas.pop(indice)

    # método para editar uma tarefa
    def editar_tarefa(self, indice, nova_descricao, nova_data):
        self.tarefas[indice].descricao = nova_descricao
        self.tarefas[indice].data = nova_data

    # método para exibir a lista de tarefas
    def exibir_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i+1}. {tarefa.descricao} - {tarefa.data}")


# Criando uma instância de lista de tarefas
lista_tarefas = ListaTarefas()

# Loop principal do programa
while True:
    # exibindo as opções disponíveis para o usuário
    print("Escolha uma opção:")
    print("1. Adicionar tarefa.")
    print("2. Excluir tarefa.")
    print("3. Editar tarefa.")
    print("4. Exibir tarefas.")
    print("5. Sair.")

    # capturando a escolha
    escolha = input()

    # adicionando uma nova tarefa
    if escolha == "1":
        descricao = input("Digite a descrição da tarefa: ")
        data = input("Digite a data da tarefa: ")
        tarefa = Tarefa(descricao, data)
        lista_tarefas.adcionar_tarefa(tarefa)

    # excluindo uma tarefa existente
    elif escolha == "2":
        indice = int(input("Digite o índice da tarefa que quer excluir: ")) - 1
        lista_tarefas.excluir_tarefa(indice)

    # editando uma tarefa
    elif escolha == "3":
        indice = int(input("Digite o índice da tarefa que quer editar: ")) - 1
        nova_descricao = input("Digite a nova descricao da tarefa: ")
        nova_data = input("Digite a nova data da tarefa: ")
        lista_tarefas.editar_tarefa(indice, nova_descricao, nova_data)

    elif escolha == "4":
        lista_tarefas.exibir_tarefas()

    elif escolha == "5":
        print("Obrigado por utilizar o gereciador de tarefas!")
        break
    else:
        print("Opção inválida. Tente novamente.")
