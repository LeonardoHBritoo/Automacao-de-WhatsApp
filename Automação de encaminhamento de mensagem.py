# Automação de encaminhamento de mensagens
# Usando funcionalidade nativa de engaminhar do Whatsapp
# Encaminhar de 5 em 5 mensagens
# Com objetivo de não deixar o Whatsapp bloquear por comportamento repetitivo
# Como atualizações constantes no Whatsapp, os XPath's e Classes dos elementos HTML devem ser subistituídos para que o código funcione

# Importande bibliotecas necessárias
from selenium import webdriver # interface do selenium que permite controlar navegadores
from selenium.webdriver.chrome.service import Service # Permite abrir e fechar chrome através do chromedriver
from webdriver_manager.chrome import ChromeDriverManager # Permite gerenciar a versão automaticamente do chrome, para o código rodar adequadamente
import time # Para realizar pausas em alguns pontos do código
from selenium.webdriver.common.keys import Keys # permite usar códigos para apertar teclas específicas do teclado
import pyperclip # Permite copiar a mensagem
from selenium.webdriver.common.action_chains import ActionChains # Permite simular ações como mover o mouse por cima de um elemento

servico = Service(ChromeDriverManager().install()) # Instala versão adequada do chromeDriver e atribui o local do arquivo para a variável
nav = webdriver.Chrome(service=servico) # Inicializa a instância do chrome controlada por selenium
nav.get('https://web.whatsapp.com/') # Acessando o site
time.sleep(120) #Tempo para realizar login de 2 min

# Mensagem deve ser subistituída 
mensagem = '''Chegou a vez da sua startup se apresentar para o ecossistema X
O evento tem como finalidade apresentar o case de 6 startups para as empresas associadas.
Acesse o formulário para mais informações. 
''' 

# Lista de contatos deve ser subistituída 
lista_contatos = ['eu','Eu Claro', 'ela','Pai']

# Enviar mensagem para o meu número e depois encaminhar 

# Clicar na lupa
nav.find_element('xpath', 'xpath da lupa').click() # Achando Xpath da lupa e clicando
# Digitar 'eu'
nav.find_element('xpath','xpath da caixa de digitar ').send_keys('eu') # Achando local para digitar e digitando
# Dar enter
nav.find_element('xpath','xpath da caixa de digitar ').send_keys(Keys.ENTER) # Teclando enter na caixa de digitar

time.sleep(1) # pausa para evitar do wpp bloquear



# Escrever a mensagem que quero encaminhar
pyperclip.copy(mensagem) # Copiando mensagem para que os emojis saiam adequadamente
nav.find_element('xpath','xpath da caixa de digitar mensagem na conversa').send_keys(Keys.CONTROL + 'V') # Colando mensagem
nav.find_element('xpath','xpath da caixa de digitar mensagem na conversa').send_keys(Keys.ENTER) # Teclando enter para enviar a mensagem

time.sleep(2) # pausa para evitar do wpp bloquear


qtde_contatos = len(lista_contatos)
if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos/5
else:
    qtde_blocos =qtde_contatos//5 + 1
for i in range(qtde_blocos):
    inicio = i * 5
    final = (i+1) * 5
    lista_envio = lista_contatos[inicio:final]
    # Encaminhar para lista de contatos
    lista_elementos = nav.find_elements('class name', 'Código da classe de mensagens no wpp(ex : _S51SS)') # Pega todos os espaços de mensagem na página/ elementos únicos na tela precisam ser achados pela classe, os demais pode ser pelo xpath
    elemento = lista_elementos[-1] # Pega localização da ultima mensagem
    ActionChains(nav).move_to_element(elemento).perform() # Move o Cursor para o bloco que contem a mensagem
    elemento.find_element('class name', 'Código da classe da setinha de opções (ex : _S51SS)').click() # Clica na setinha
    time.sleep(0.5)

    nav.find_element('xpath', 'xpath do elemento encaminhar').click() # Clica em encaminhar
    nav.find_element('xpath', 'xpath da setinha encaminhar').click() # Clica na seta para confirmar encaminhamento
    time.sleep(1)
    for nome in lista_envio:
        nav.find_element('xpath','xpath da caixa de busca de contatos').send_keys(nome) # Procura contato
        time.sleep(1.2)
        nav.find_element('xpath','xpath da caixa de busca de contatos').send_keys(Keys.ENTER) # Da enter
        time.sleep(1.1)
        nav.find_element('xpath','xpath da caixa de busca de contatos').send_keys(Keys.BACKSPACE) # Apaga texto da caixa de busca 
        time.sleep(1)
    nav.find_element('xpath', 'xpath do botão de enviar').click()
    time.sleep(3)