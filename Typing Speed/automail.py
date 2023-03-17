import smtplib

# Configurações do email
sender_email = "seu_email@gmail.com"
sender_password = "sua_senha"
receiver_email = "email_do_destinatario@gmail.com"
subject = "Assunto do email"
body = "Corpo do email"

# Conectar-se ao servidor SMTP do Gmail
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(sender_email, sender_password)

# Cria o corpo do email
msg = f'Subject: {subject}\n\n{body}'

# Envia o email
smtp_server.sendmail(sender_email, receiver_email, msg)

# Fecha a conexão
smtp_server.quit()
