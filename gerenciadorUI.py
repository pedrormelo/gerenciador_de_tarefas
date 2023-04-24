import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Tarefa:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data


class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adcionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def excluir_tarefa(self, indice):
        self.tarefas.pop(indice)

    def editar_tarefa(self, indice, nova_descricao, nova_data):
        self.tarefas[indice].descricao = nova_descricao
        self.tarefas[indice].data = nova_data

    def exibir_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            tarefa_str = f"{i+1}. {tarefa.descricao} - {tarefa.data}"
            lista_box.insert(tk.END, tarefa_str)


lista_tarefas = ListaTarefas()


def adicionar_tarefa():
    descricao = descricao_entry.get()
    data = data_entry.get()
    tarefa = Tarefa(descricao, data)
    lista_tarefas.adcionar_tarefa(tarefa)
    lista_box.delete(0, tk.END)
    lista_tarefas.exibir_tarefas()


def excluir_tarefa():
    indice = lista_box.curselection()
    if indice:
        lista_tarefas.excluir_tarefa(indice[0])
        lista_box.delete(indice)


def editar_tarefa():
    indice = lista_box.curselection()
    if indice:
        descricao_antiga = lista_tarefas.tarefas[indice[0]].descricao
        data_antiga = lista_tarefas.tarefas[indice[0]].data
        nova_descricao = simpledialog.askstring(
            "Editar tarefa", "Nova descrição:", initialvalue=descricao_antiga)
        nova_data = simpledialog.askstring(
            "Editar tarefa", "Nova data:", initialvalue=data_antiga)
        if nova_descricao and nova_data:
            lista_tarefas.editar_tarefa(indice[0], nova_descricao, nova_data)
            lista_box.delete(0, tk.END)
            lista_tarefas.exibir_tarefas()


def confirmar_saida():
    if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
        janela.destroy()


janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

# Campos para adicionar tarefa
descricao_label = tk.Label(janela, text="Descrição:")
descricao_label.grid(row=0, column=0, padx=5, pady=5)
descricao_entry = tk.Entry(janela)
descricao_entry.grid(row=0, column=1, padx=5, pady=5)
data_label = tk.Label(janela, text="Data:")
data_label.grid(row=1, column=0, padx=5, pady=5)
data_entry = tk.Entry(janela)
data_entry.grid(row=1, column=1, padx=5, pady=5)
adicionar_button = tk.Button(
    janela, text="Adicionar", command=adicionar_tarefa)
adicionar_button.grid(row=2, column=1, padx=5, pady=5)

# Lista de tarefas
lista_box = tk.Listbox(janela)
lista_box.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
excluir_button = tk.Button(janela, text="Excluir", command=excluir_tarefa)
excluir_button.grid(row=4, column=0, padx=5, pady=5)

# Botão para editar tarefa
editar_button = tk.Button(janela, text="Editar", command=editar_tarefa)
editar_button.grid(row=4, column=1, padx=5, pady=5)

# Confirmação de saída
janela.protocol("WM_DELETE_WINDOW", confirmar_saida)

janela.mainloop()
