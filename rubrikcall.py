# Basierend auf senden.py von DF7FL (Phillip)   https://github.com/DL7FL
# weiterentwickelt von DG5GSA (Stefan)          https://github.com/dg5gsa
# Version 1.0 - Stand 13.05.2018

# Mit diesem Script kann eine Nachricht in eine Rubrik geschrieben werden,
# entsprechende Schreibrechte müssen vorher über ein Ticket bei den Admins
# von www.hampager.de beantragt werden.

# Die Datei dapnet.py muss sich zwingend im gleichen Verzeichnis befinden.



# Anpassungen sind mit Komentaren markiert


import os
import dapnet
import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s,%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

login = 'DeinUsername'                      # Hier deinen Usernamen einfügen
passwd = 'DeinSehrGeheimesPasswort'         # Hier dein Passwort einfügen

url = 'http://hampager.de:8080/news'        # Diese Adresse nimmt Rubrik Nachrichten entgegen, nicht ändern !!
rubricName = 'ogeminfo'                     # hier den Rubriknamen eintragen

number = '5'                                # Hier den Speicherplatz der Nachricht eintragen, 1 bis 9 möglich
text = 'Rubrik OG EM Info befindet sich im Testbetrieb. Meldungen an DG5GSA'      # Text der in die Rubrik geschrieben werden soll

dapnet.PUT(text, rubricName, number, login, passwd, url, )      

