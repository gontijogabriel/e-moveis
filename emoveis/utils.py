import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings

def mandaEmail(token, destinatario, assunto, nome_do_usuario):
    # Configurar o objeto do e-mail
    email_msg = MIMEMultipart()
    email_msg['From'] = settings.EMAIL_HOST_USER
    email_msg['To'] = destinatario
    email_msg['Subject'] = assunto

    # Criar o corpo do e-mail em HTML com o token
    message = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redefinição de Senha</title>
        </head>
        <body>
            <p>Olá {nome_do_usuario},</p>
            <p>Você solicitou a redefinição de senha. Este é seu token para redefinir sua senha:</p>
            
            <p>{token}</p>
            
            <p>Se você não solicitou a redefinição de senha, ignore este e-mail.</p>
            <p>Atenciosamente,<br>
            e-moveis</p>
        </body>
        </html>
    """

    # Adicionar o corpo do e-mail ao objeto do e-mail
    email_msg.attach(MIMEText(message, 'html'))

    # Configurar e conectar ao servidor SMTP
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

    # Enviar o e-mail
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    # Fechar a conexão com o servidor SMTP
    server.quit()
    print('Mensagem enviada!')
