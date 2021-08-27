import pyautogui #mouse e teclado
import time
import pyperclip #ctrl+c e v com pyper.

#pyautogui.. serve para qualquer tecla com a win e pode coloca o texto direto, é dahora!
# PAUSE significa pausar e na frente você coloca o tempo que quiser 1 = segundo, 60 segundos = 1 minuto

pyautogui.PAUSE = 1
# ele da um ALERTA!!!
pyautogui.alert('NÃO MEXE,EU ESTOU USANDO O PC DEPOIS VOCÊ VOLTA')

pyautogui.hotkey('win','2')  # nesse caso é para abrir o chrome, mas pode ser que o seu chrome nao esteja nessa posição
# caso você esteja abrindo pelo jupyter anaconda deixe isso como comentário, caso contrario coloque no espaço da
# tecla. win, 2.
