import tkinter as tk
from tkinter import filedialog, messagebox


class RunScreen(tk.Frame):
    def __init__(self, master, voltar_menu, automation):
        super().__init__(master)
        self.master = master
        self.voltar_menu = voltar_menu
        self.automation_controller = automation
        self.init_ui()

    def init_ui(self):
        # Configurar layout do Frame para centralizar os elementos
        self.grid_rowconfigure(0, weight=1)  # Espaço acima
        self.grid_rowconfigure(1, weight=1)  # Linha para o campo de link
        self.grid_rowconfigure(2, weight=1)  # Linha para o botão "Carregar Excel"
        self.grid_rowconfigure(3, weight=1)  # Linha para o botão "Voltar"
        self.grid_rowconfigure(4, weight=1)  # Espaço abaixo
        self.grid_columnconfigure(0, weight=1)  # Centralizar horizontalmente

        # Campo de entrada para o link
        tk.Label(self, text="Link para enviar aos clientes:").grid(row=1, column=0, pady=5)
        self.link_entry = tk.Entry(self, width=40)  # Definindo uma largura fixa
        self.link_entry.grid(row=2, column=0, pady=5, padx=50, sticky="ew")

        # Botão "Carregar Excel"
        tk.Button(self, text="Carregar Excel", command=self.carregar_excel).grid(
            row=3, column=0, pady=10
        )

        # Botão "Voltar"
        tk.Button(self, text="Voltar", command=self.voltar_menu).grid(
            row=4, column=0, pady=10
        )

    def carregar_excel(self):
        # Obter o link do campo de entrada
        link = self.link_entry.get().strip()

        # Verificar se o link foi preenchido
        if not link:
            messagebox.showwarning("Aviso", "Por favor, insira um link antes de carregar o Excel.")
            return

        # Abrir diálogo para selecionar arquivo Excel
        file_path = filedialog.askopenfilename(
            title="Selecione o arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx *.xls")],
        )
        if file_path:
            # Executa a lógica da automação
            try:
                self.automation_controller.run(file_path, link)
                messagebox.showinfo("Execução Terminada", "Execução finalizada.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao executar automação: {str(e)}")
        else:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")