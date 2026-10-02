#UMA API É UM JEITO CONECTAR SISTEMAS, INTERFACE DE PROGRAMAÇÃO DE APLICAÇÕES;
#API É UM CONJUNTO DE REGRAS E PADRÕES QUE PERMITE QUE DIFERENTE SISTEMAS
#DE SOFTWARE SE COMUNIQUEM E TROQUEM DADOS ENTRE SI;

#NESTE, SERÁ UTILIZADA A WEATHERapi.com PARA CONSULTAR AS CONDIÇÕES 
#CLIMÁTICAS DE UMA LOCALIDADE;

#CONSUMIR API ->
#VAMOS PRECISAR DE UMA PROGRAMA QUE TENHA UMA CERTA CAPACIDADE DE PEGAR DADOS
#MEDIANTE A UMA URL PRÉ DEFINIDA

#VAMOS PRECISAR DA APIKEY
import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir dados de forma legível
api_key = "5403842e2e284a99a44224514262909"

link_api = "http://api.weatherapi.com/v1/current.json"
cidade = input("Digite o nome da cidade: ")
qualidade_ar = input("Deseja consultar a qualidade do ar? (sim/não): ")

# Define se envia 'yes' ou 'no' de acordo com a resposta do utilizador
obter_aqi = "yes" if qualidade_ar.strip().lower() in ["sim", "s"] else "no"

parametros = {
    "key": api_key,
    "q": cidade,        # Utiliza a variável 'cidade' sem aspas
    "aqi": obter_aqi,   # Passa 'yes' para obter os dados da qualidade do ar
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    print("Requisição bem sucedida!")
    dados = resposta.json()
    temperatura = dados["current"]["temp_c"]
    condicao = dados["current"]["condition"]["text"]
    
    print(f"A temperatura atual em {cidade} é de {temperatura}°C e a condição do tempo é: {condicao}.")
    
    # Exibe as informações da qualidade do ar caso tenham sido solicitadas
    if obter_aqi == "yes" and "air_quality" in dados["current"]:
        aqi_dados = dados["current"]["air_quality"]
        
        indice_epa = aqi_dados.get("us-epa-index")
        pm2_5 = aqi_dados.get("pm2_5")
        pm10 = aqi_dados.get("pm10")
        
        print(f"Índice de Qualidade do Ar (US EPA): {indice_epa}")
        print(f"Partículas PM2.5: {pm2_5} µg/m³")
        print(f"Partículas PM10: {pm10} µg/m³")
else:
    print("Erro na requisição. Código de status:", resposta.status_code)