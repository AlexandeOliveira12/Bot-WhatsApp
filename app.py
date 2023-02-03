
# Importar libs
import pywhatkit
import keyboard
import time
from datetime import datetime
from decouple import config

# Definir contatos
contatos = [config('Telefone1'), config('Telefone2')]

#Intervalo de Envio
while len(contatos) >= 2:
    pywhatkit.sendwhats_image(contatos[0], 'img.png', 'Manutenção de Desktop e Notebooks, formatação e limpeza de hardware', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(30)
    keyboard.press_and_release('ctrl + w')

#'+5518981392300' Bruno
#'+5518991815959' Prof Silvana
#'+5518997407367' Tio Rafa
#'+5518981577828' Ana tutora
