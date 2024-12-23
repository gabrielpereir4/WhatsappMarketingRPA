from controller.automation import Automation
from view.main_screen import MainScreen
from view.run_screen import RunScreen
from view.db_screen import DBScreen
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



VERSION = '0.5.0'

class App(tk.Tk):
    def __init__(self):
        self.automation_controller = Automation()
        super().__init__()
        self.title("Whatsapp AJFILHO")
        self.geometry("400x300")
        self.center_window(400, 300)  # Centraliza a janela
        #slf.set_window_icon("assets/logotipo.png")
        self.resizable(False, False)  # Desativa o redimensionamento
        self.tela_principal = None
        self.tela_excel = None
        self.tela_banco = None
        self.init_ui()


    def center_window(self, width, height):
        """Centraliza a janela na tela."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")


    """
    def set_window_icon(self, icon_path):
        Define o ícone da janela do Tkinter
        try:
            icon_image = Image.open(icon_path).resize((16, 16)) # Redimensiona para 32x32 pixels
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.iconphoto(False, icon_photo)
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Não foi possível carregar o ícone: {e}")
    """

    def init_ui(self):
        """Inicializa a interface gráfica."""
        self.tela_principal = MainScreen(self, self.show_tela_excel, self.show_tela_banco, self.show_guia, VERSION)
        self.tela_principal.pack(fill="both", expand=True)  # Ocupa todo o espaço disponível

    def show_tela_excel(self):
        """Exibe a tela de execução da automação."""
        self.tela_principal.pack_forget()
        if not self.tela_excel:
            self.tela_excel = RunScreen(self, self.voltar_menu, self.automation_controller)
        self.tela_excel.pack(fill="both", expand=True)

    def show_tela_banco(self):
        """Exibe a tela de banco de dados."""
        #self.tela_principal.pack_forget()
        if not self.tela_banco:
            #self.tela_banco = DBScreen(self, self.voltar_menu)
            messagebox.showwarning("Não Implementado", "Essa funcionalidade ainda não está disponível.")
        #self.tela_banco.pack(fill="both", expand=True)

    def show_guia(self):
        """Exibe a guia para o Excel."""
        # Exibir uma nova janela com a guia para Excel
        largura = 400
        altura = 250

        guia_window = tk.Toplevel(self)
        guia_window.title("Guia para Excel")
        self.center_child_window(guia_window, largura, altura)  # Centraliza a janela

        # Conteúdo da janela
        tk.Label(guia_window, text="Guia para Excel (Padrão Aceito):", font=("Arial", 12, "bold")).pack(pady=8)
        tk.Label(guia_window, text="ID - Nome - Número", font=("Arial", 10)).pack(pady=5)
        tk.Label(guia_window, text="ID pode ser um campo vazio.", font=("Arial", 10)).pack(pady=8)

        # Botão para fechar a janela
        tk.Button(guia_window, text="Fechar", command=guia_window.destroy).pack(pady=20)


    def center_child_window(self, window, width, height):
        """Centraliza uma janela filha (Toplevel) em relação à tela."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def voltar_menu(self):
        """Volta para a tela principal."""
        if self.tela_excel:
            self.tela_excel.pack_forget()
        if self.tela_banco:
            self.tela_banco.pack_forget()
        self.tela_principal.pack(fill="both", expand=True)  # Ocupa todo o espaço disponível


if __name__ == "__main__":
    app = App()
    app.mainloop()