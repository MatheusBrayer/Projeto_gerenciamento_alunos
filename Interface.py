import tkinter as tk
from tkinter import ttk, messagebox
import Banco

Banco.conectar_db()

root = tk.Tk()
root.title("Sistema de Alunos")
root.geometry("600x600")
root.resizable(False, False)

frame_cadastro = tk.LabelFrame(root, text="Cadastrar/Atualizar Aluno", padx=10, pady=10)
frame_cadastro.pack(padx=10, pady=10, fill="x")


label_nome = tk.Label(frame_cadastro, text="Nome:")
label_nome.grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame_cadastro, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)


label_email = tk.Label(frame_cadastro, text="Email:")
label_email.grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_cadastro, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5)


label_telefone = tk.Label(frame_cadastro, text="Telefone:")
label_telefone.grid(row=2, column=0, sticky="w")
entry_telefone = tk.Entry(frame_cadastro, width=40)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

id_atual = None

def cadastrar():
    global id_atual
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome == '' or telefone == '':
        messagebox.showwarning('Atenção!', 'Nome e telefone são obrigatórios!')
        return

    if id_atual:
        Banco.atualizar_aluno(id_atual, nome, email, telefone)
        messagebox.showinfo('Sucesso', 'Aluno atualizado com sucesso!')
        id_atual = None
        botao_cadastrar.config(text="Cadastrar")
    else:
        Banco.cadastrar_aluno(nome, email, telefone)
        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')

    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    carregar_alunos()


botao_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", width=20, command=cadastrar)
botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

frame_lista = tk.LabelFrame(root, text="Lista de Alunos", padx=10, pady=10)
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

colunas = ("id", "nome", "email", "telefone")
tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=100)

tree.pack(fill="both", expand=True)


def carregar_alunos():
    for item in tree.get_children():
        tree.delete(item)
    alunos = Banco.listar_alunos()
    for aluno in alunos:
        tree.insert("", "end", values=aluno)


carregar_alunos()


def excluir():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Atenção!", "Selecione um aluno para excluir.")
        return
    id_aluno = tree.item(item_selecionado[0])["values"][0]
    Banco.excluir_aluno(id_aluno)
    messagebox.showinfo("Sucesso!", "Aluno excluído com sucesso.")
    carregar_alunos()


botao_excluir = tk.Button(root, text="Excluir Selecionado", width=20, command=excluir)
botao_excluir.pack(pady=5)


def editar():
    global id_atual
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Atenção!", "Selecione um aluno para editar.")
        return
    dados = tree.item(item_selecionado[0])["values"]
    id_atual = dados[0]
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_nome.insert(0, dados[1])
    entry_email.insert(0, dados[2])
    entry_telefone.insert(0, dados[3])
    botao_cadastrar.config(text="Atualizar")


botao_editar = tk.Button(root, text="Editar Selecionado", width=20, command=editar)
botao_editar.pack(pady=5)

root.mainloop()
