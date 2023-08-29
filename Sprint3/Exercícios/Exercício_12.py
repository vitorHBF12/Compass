import json

with open('person.json', 'r') as meu_json:
    dados = json.load(meu_json)
    print(dados)
