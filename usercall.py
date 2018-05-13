# Basierend auf senden.py von DF7FL (Phillip)   https://github.com/DL7FL
# weiterentwickelt von DG5GSA (Stefan)          https://github.com/dg5gsa
# Version 1.0 - Stand 13.05.2018

# Mit diesem Script kann eine Nachricht direkt an einen, oder mehrere User
# geschickt werden. Usercalls werden mit ["Call",] getrennt und dann vom
# Script in Einzelrufe aufgesplittet. 

# Die Datei dapnet.py muss sich zwingend im gleichen Verzeichnis befinden.


# Anpassungen sind mit Komentaren markiert

import os
import dapnet
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s,%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

login = 'DeinCall'                            # Hier den Dapnet Username eintragen
passwd = 'DeinSuperGeheimesPasswort'          # Hier das Dapnet Passwort eintragen

url = 'http://hampager.de:8080/calls'         # Diese Adress nimmt User Calls entgegen, nicht verändern.

text = 'Testruf ueber ein kleines Python Script'  # Hier den Text der Nachricht eingeben
callsign_list = ["dg5gsa", "dg5gsa"]              # Hier die Empfänger der Nachricht eingeben
txgroup = "dl-all"                                # Hier die Sender Gruppe eintragen über die gesendet werden soll

dapnet.send(text, callsign_list, login, passwd, url, txgroup)

