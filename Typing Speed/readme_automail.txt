Primeiro, importamos a biblioteca smtplib, que nos permitirá enviar o email.

Em seguida, definimos algumas variáveis para configurar o email: o endereço de email do remetente, a senha do remetente, o endereço de email do destinatário, o assunto e o corpo do email.

Depois, usamos o método smtplib.SMTP() para conectar-se ao servidor SMTP do Gmail na porta 587. Também usamos o método starttls() para criptografar a conexão.

Em seguida, usamos o método login() para fazer login no servidor SMTP do Gmail usando o endereço de email do remetente e a senha.

Então, criamos o corpo do email, formatando o assunto e o corpo do email em uma única string.

Por fim, usamos o método sendmail() para enviar o email, especificando o endereço de email do remetente, o endereço de email do destinatário e o corpo do email. Em seguida, usamos o método quit() para desconectar-se do servidor SMTP.

Lembre-se de habilitar a opção "Permitir aplicativos menos seguros" nas configurações da sua conta do Gmail para permitir que o script se conecte ao servidor SMTP do Gmail.