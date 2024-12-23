import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, master, show_tela_excel, show_tela_banco, show_guia, version):
        super().__init__(master)
        self.master = master
        self.show_tela_excel = show_tela_excel
        self.show_tela_banco = show_tela_banco
        self.show_guia = show_guia
        self.version = version  # Versão passada como parâmetro
        self.init_ui()

    def init_ui(self):
        # Configura o layout para centralização
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Botão Executar Automação
        tk.Button(self, text="Executar Automação", command=self.show_tela_excel).grid(
            row=0, column=0, pady=10
        )

        # Botão Carregar/Visualizar Mensagens
        tk.Button(self, text="Carregar/Visualizar Mensagens", command=self.show_tela_banco).grid(
            row=1, column=0, pady=10
        )

        # Botão "Guia para Excel"
        tk.Button(self, text="Guia para Excel", command=self.show_guia).grid(
            row=2, column=0, pady=10
        )

        # Label "Versão" no canto inferior direito
        label_version = tk.Label(self, text=f"Versão: {self.version}")
        label_version.grid(row=3, column=0, sticky="se", padx=10, pady=10)
