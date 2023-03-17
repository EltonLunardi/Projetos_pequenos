import time


def typing_speed():
    text = input("Digite o texto: ")
    start_time = time.time()
    input_text = input("Digite o texto novamente: ")
    end_time = time.time()
    time_taken = end_time - start_time
    words = len(text.split())
    wpm = words / (time_taken / 60)
    accuracy = calculate_accuracy(text, input_text)
    print("Você digitou {} palavras em {:.2f} segundos.".format(words, time_taken))
    print("Sua velocidade de digitação é de {:.2f} WPM.".format(wpm))
    print("Sua precisão de digitação é de {:.2f}%.".format(accuracy))


def calculate_accuracy(text, input_text):
    correct_chars = 0
    for i in range(len(text)):
        if i >= len(input_text):
            break
        if text[i] == input_text[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(text)) * 100
    return accuracy


typing_speed()

'''
Primeiro, importamos a biblioteca smtplib, que nos permitirá enviar o email.

Em seguida, definimos algumas variáveis para configurar o email: o endereço de email do remetente, a senha do remetente, o endereço de email do destinatário, o assunto e o corpo do email.

Depois, usamos o método smtplib.SMTP() para conectar-se ao servidor SMTP do Gmail na porta 587. Também usamos o método starttls() para criptografar a conexão.

Em seguida, usamos o método login() para fazer login no servidor SMTP do Gmail usando o endereço de email do remetente e a senha.

Então, criamos o corpo do email, formatando o assunto e o corpo do email em uma única string.

Por fim, usamos o método sendmail() para enviar o email, especificando o endereço de email do remetente, o endereço de email do destinatário e o corpo do email. Em seguida, usamos o método quit() para desconectar-se do servidor SMTP.

Lembre-se de habilitar a opção "Permitir aplicativos menos seguros" nas configurações da sua conta do Gmail para permitir que o script se conecte ao servidor SMTP do Gmail.
'''