from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Indique o caminho do arquivo driver do Brave
brave_path = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application'
driver_path = 'C:/path/to/brave/driver'

# Configura as opções do Brave
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Inicializa o driver do Brave
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Inicializa o driver do Chrome
#driver = webdriver.Chrome()

# Navega até o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Aguarda o usuário fazer o login no WhatsApp Web manualmente
input("Faça login no WhatsApp Web e pressione Enter para continuar...")

# Seleciona a conversa com a pessoa ou grupo desejado
chat_name = "Nome do contato ou grupo"
search_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
search_box.send_keys(chat_name)
search_box.send_keys(Keys.ENTER)

# Aguarda a mensagem recebida
wait = WebDriverWait(driver, 600)
last_message = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "div.message-in")))

# Responde com uma mensagem automática
response = "Mensagem automática"
message_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
message_box.send_keys(response)
message_box.send_keys(Keys.ENTER)

# Fecha o navegador
driver.quit()

'''
Primeiro, importamos a classe webdriver da biblioteca Selenium.

Em seguida, indicamos o caminho do arquivo executável do Brave no sistema operacional e o caminho do arquivo driver do Brave. O arquivo driver é responsável por controlar o navegador e permitir a automação do navegador.

Configuramos as opções do Brave usando o método ChromeOptions() da classe webdriver. Usamos o atributo binary_location para especificar o caminho do arquivo executável do Brave.

Finalmente, inicializamos o driver do Brave usando o método Chrome() da classe webdriver. Passamos o caminho do arquivo driver do Brave como argumento para o parâmetro executable_path e as opções do Brave como argumento para o parâmetro options.

Certifique-se de baixar a versão correta do arquivo driver para o seu sistema operacional e versão do Brave. Além disso, lembre-se de atualizar os caminhos dos arquivos executáveis do Brave e do driver de acordo com a localização dos arquivos em seu sistema.
'''