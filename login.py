import requests
import json

LOGIN_URL = "https://saude.sulamericaseguros.com.br/prestador/login"
HOME_URL = "https://saude.sulamericaseguros.com.br/prestador/"
SERVICOS_MEDICOS_URL = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/"
FATURAMENTO_URL = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/"
GUIA_CONSULTA_URL = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/"
BUSCA_PACIENTE_URL = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/guia-de-consulta-incluir.htm"

payload = {
    "codigoIndentificacao": "100000009361",
    "usuario": "master",
    "senha": "837543"
}

payload_busca = {
    "busca_paciente" : "55788888485177660015"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Referer": "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

session = requests.Session()

response = session.post(LOGIN_URL, data=payload)

if "Bem-vindo" in response.text or response.status_code == 200:
    print("Login realizado com sucesso!")
else:
    print("Falha no login. Verifique as credenciais.")
    exit()


paginas = [HOME_URL, SERVICOS_MEDICOS_URL, FATURAMENTO_URL, GUIA_CONSULTA_URL]
for pagina in paginas:
    response = session.get(pagina)
    print(f"Acessando: {pagina} - Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Erro ao acessar {pagina}")
        exit()

response = session.post(BUSCA_PACIENTE_URL, data=payload_busca, headers=headers, cookies=session.cookies)

if response.status_code == 200 and "Portal" in response.text:
    print("Paciente localizado com sucesso!")
else:
    print("Erro ao buscar o paciente.")