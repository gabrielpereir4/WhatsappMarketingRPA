import pandas as pd
import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tasks:
    def __init__(self):
        self.driver = None
        self.df = None

    def send_messages(self, sendlink):
        """
        Envia mensagens para os contatos do arquivo Excel
        """
        skip = 0

        for linha in range(len(self.df)):
            nome = self.df.iloc[linha, 1]  # Coluna 'Nome'
            if nome is None or pd.isna(nome):
                print(f"Skipping name {self.df.iloc[linha, 1]}")
                skip = skip + 1
                continue
            #print(f'Nome antes de limpar {nome}')
            nome = self.clean_name(nome)

            numero = self.df.iloc[linha, 2]  # Coluna 'Número'
            numero = self.clean_number(numero)
            if numero is None or pd.isna(numero):
                print(f"Skipping number {self.df.iloc[linha, 2]} ({numero})")
                skip = skip + 1
                continue

            #print(f"Linha {linha}: Nome={nome}, Número={numero}")
            

            greeting = self.random_greeting(nome)
            message = (greeting + " Temos ofertas de consórcio especiais para você!\n"
            f" Confira o link a seguir: {sendlink}")
            print(message, f"+55{numero}")
            try:
                self.send_message(f"+55{numero}", message)
                #pywhatkit.sendwhatmsg_instantly(f"+{numero}", message, wait_time=30)
            except Exception:
                print(f"Erro ao enviar mensagem para {nome} ({numero})")
                continue

        print(f'Skipped {skip} out of {len(self.df)}')
        self.driver.quit()

    def read_excel(self, filepath):
        """
        Lê um arquivo Excel e retorna um DataFrame Pandas
        """
        self.df = pd.read_excel(filepath, skiprows=0)
        print(self.df)
        return self.df


    def random_wait(self):
        """
        Aguarda um tempo aleatório entre 5 e 15 segundos
        """
        time.sleep(random.randint(5, 15))


    def random_greeting(self, name):
        """
        Retorna uma saudação aleatória com o nome do contato
        """
        choice = random.randint(1, 3)
        if choice == 1:
            return f"Olá {name}!"
        elif choice == 2:
            return f"{name}, tudo bem?"
        elif choice == 3:
            return f"{name}, como vai?"
        

    def clean_number(self, valor):
        """
        Limpa valores de telefone, removendo caracteres especiais e mantendo apenas números para envio de mensagem
        """
        if not valor or valor in ["Sem telefone", "Nenhum telefone informado"]:
            return None

        # Remove caracteres não numéricos e captura apenas números
        numeros = re.findall(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', str(valor))
        #print(f"Números encontrados: {numeros}")

        # Itera sobre os números encontrados
        for numero in numeros:
            # Remove caracteres como parênteses, espaços e traços para validar o número
            numero_limpo = re.sub(r'\D', '', numero)  # Remove tudo que não for dígito
            if len(numero_limpo) == 11 and numero_limpo[2] == '9':  # Verifica celular válido
                #print(f"Número válido encontrado: {numero_limpo}")
                return numero_limpo

        return None
    
    def clean_name(self, name):
        """
        Limpa o nome do contato, deixando apenas o primeiro nome com a primeira letra maiúscula
        """
        try:
            parts = name.split()
            #print(f'parts: {parts}')
            # Se houver pelo menos uma parte, manipular o primeiro nome
            if parts:
                # Transformar a primeira letra do primeiro nome em maiúscula e o restante em minúscula
                parts[0] = parts[0].capitalize()

            # Unir todas as partes do nome, com o primeiro nome formatado
            nome_limpo = parts[0]
                    
            return nome_limpo
        except:
            return name


    def open_whatsapp(self):
        # Configurar WebDriver (certifique-se de ter o ChromeDriver instalado)
        self.driver = webdriver.Chrome()

        # Acesse o WhatsApp Web e faça login
        self.driver.get("https://web.whatsapp.com")
        return self.driver

    def send_message(self, phone_number, message):
        url = f"https://web.whatsapp.com/send?phone={phone_number}&text={message}"
        self.driver.get(url)
        time.sleep(5)  # Aguarde o carregamento da página
        send_button = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        time.sleep(2)  # Aguarde o envio da mensagem

