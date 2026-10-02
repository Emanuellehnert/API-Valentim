import requests 





menu_moedas = """

=== Opções de Moedas para Consulta ===

Tradicionais:

USD-BRL (Dólar Americano)
EUR-BRL (Euro)
GBP-BRL (Libra Esterlina)
ARS-BRL (Peso Argentino)

Criptomoedas:

BTC-BRL (Bitcoin)
ETH-BRL (Ethereum)

=====================================

"""


def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        print("Deu certo")
        print(resposta.json())
        return resposta.json()
    elif resposta.status_code == 404:
        print("Aconteceu um erro na sua requisição. Verifique se a moeda está correta.")
        error = resposta.json()
        status = error["status"]
        codigo = error["code"]
        mensagem = error["message"]
        print(f"Status: {status}")
        print(f"Código: {codigo}")
        print(f"Mensagem: {mensagem}")
        return resposta.json()
    else:
        print("Deu errado")

moeda_desejada = input("Digite a moeda desejada (ex: USD-BRL): ")

dados_api = consultar_moeda(moeda_desejada)

#---------------------------------------------------- tratamento do json--------------------------
if dados_api:
    
    valor = list(dados_api.values())[0]["bid"]

    print("\nRequisição bem-sucedida!")
    
    print(f"O valor atual de {moeda_desejada} é:")
    print(f"R$ {float(valor):.2f}")

else:
    print(f"\nErro ao consultar a moeda: {moeda_desejada} \nVerifique se o formato esta correto")