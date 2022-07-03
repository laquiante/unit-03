#!/usr/bin/python3

# Benutzer: cumulus im Home-Verzeichnis
# source testumgebung/bin/activate

from flask import Flask
from flask import render_template

import requests
import urllib3

SWITCHE = ["192.168.200.2","192.168.200.3"]

# nicht schoen aber heute Nachmittag zweckmaessig
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def start():
    ergebnis = requests.get('https://192.168.200.2:8765/cue_v1/bridge/domain/alq/mac-table', auth=('cumulus','CumulusLinux!'), verify=False)
    return render_template("home.html", ergebnis=os_liste)

app.run(host='::',debug=True)