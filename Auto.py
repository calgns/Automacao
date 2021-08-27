import pyautogui #mouse e teclado
import time
import pyperclip #ctrl+c e v com pyper.

#pyautogui.. serve para qualquer tecla com a win e pode coloca o texto direto, é dahora!
# PAUSE significa pausar e na frente você coloca o tempo que quiser 1 = segundo, 60 segundos = 1 minuto

pyautogui.PAUSE = 1
# ele da um ALERTA!!!
pyautogui.alert('NÃO MEXE,EU ESTOU USANDO O PC DEPOIS VOCÊ VOLTA')

pyautogui.hotkey('win',"shift",'2')# nesse caso é para abrir o chrome,
# mas pode ser que o seu chrome não esteja nessa posição
# caso você esteja abrindo pelo jupyter anaconda deixe isso como comentário, caso contrario coloque no espaço da
# tecla. win, 2. e caso não funcione tire o shift.

link = r"https://mail.google.com/"
#copiando o link
pyperclip.copy(link)

# colando o link
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
# nesse caso o link e do gmail, mas poderia ser qualquer outro

# no caso de usar o pycharm use o comando win up para deixa-lo em tela cheia
pyautogui.hotkey("win",'up')

# time.sleep para  dar tempo do site carregar
time.sleep(5)

# nesse paso você tera que descobrir a posição do mouse para apertar em escrever no gmail
#  o comando utilizado seria. print(pyautogui.position()) você usara este comando
#  quando estiver com o mouse em cima do botão.
# no meu caso deu essa posição, então é melhor que você descubra a sua
pyautogui.click(107, 202)
# time.sleep para carregar ao invés de time sleep você pode usar o Pause se quiser.
time.sleep(1)
#curiosidade da pra escolher quantidade de clicks:pyautogui.click(107, 202,clicks = 200)

# copiando o email da lisa
email = 'MonaLisa+nãoleia@gmail.com'
pyperclip.copy(email)

#dando tempo para recarregar o site
time.sleep(5)
# colando
pyautogui.hotkey('ctrl', 'v')
# passando para assunto
pyautogui.hotkey('tab')

# copiado assunto
assunto = """
assunto
qualquer coisa
....
num sei 
....
"""
pyperclip.copy(assunto)