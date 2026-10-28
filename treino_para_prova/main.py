
import requests


nome = input("Digite o nome do Pokémon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    print(f"Pokémon: {dados['name']}")
    print(f"ID: {dados['id']}")
    print(f"Altura: {dados['height']}")
    print(f"Peso: {dados['weight']}")
else:
    print("Não foi possível consultar o Pokémon.")