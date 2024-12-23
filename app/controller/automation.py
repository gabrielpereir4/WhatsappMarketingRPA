from model.tasks import Tasks
from tkinter import messagebox

class Automation():
    def __init__(self):
        self.Tasks = Tasks()


    def run(self, filepath, link):
        self.Tasks.read_excel(filepath)
        self.Tasks.open_whatsapp()
        self.show_qr_code_message()
        self.Tasks.send_messages(link)

    def show_qr_code_message(self):
        # Mostrar a MessageBox
        messagebox.showinfo("QR Code", "Escaneie o QR Code no WhatsApp Web e clique em OK para continuar.")