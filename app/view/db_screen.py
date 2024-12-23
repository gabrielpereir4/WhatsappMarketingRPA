import tkinter as tk
from tkinter import messagebox

# Tela de Banco de Dados
class DBScreen(tk.Frame):
    def __init__(self, master, voltar_menu):
        super().__init__(master)
        self.master = master
        self.voltar_menu = voltar_menu
        self.init_ui()

    def init_ui(self):
        tk.Label(self, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        tk.Label(self, text="ID:").pack(pady=5)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=5)

        tk.Label(self, text="Valor:").pack(pady=5)
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack(pady=5)

        tk.Button(self, text="Enviar Dados", command=self.enviar_dados).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar_menu).pack(pady=10)

    def enviar_dados(self):
        nome = self.entry_nome.get()
        id_ = self.entry_id.get()
        valor = self.entry_valor.get()

        if nome and id_ and valor:
            # Simular envio ao banco
            messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")