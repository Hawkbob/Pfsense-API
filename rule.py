import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Altere if= para o nome da sua interface
url_pfsense = "https://seuip/api/v2/firewall/rules?if=SUAINTERFACE&descr=tmp"
apply_pfsense = "https://seuip/api/v2/firewall/apply"

token_pfsense = {"X-API-Key": "TOKEN_AQUI"}

print("Removendo Regras pfSense... \r\n")
response = requests.delete(url_pfsense, headers=token_pfsense, verify=False)
data = response.json()
print(data, "\n")

print("Enviando Apply... \r\n")
apply = requests.post(apply_pfsense, headers=token_pfsense, verify=False)
