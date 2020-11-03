import requests

URL = 'http://lad.ufcg.edu.br/loac/uploads/OAC/anon.txt'
response = requests.get(URL)

with open('anon.txt', 'w') as file:
    file.write(response.text)

with open('anon.txt', 'r') as file:
    dict_apelidos = {}
    for linha in file.readlines():
        [identificador, _, centavos, *_] = linha.split() 
        
        if identificador not in dict_apelidos:
            dict_apelidos[identificador] = []

        dict_apelidos[identificador].append(int(centavos))

    apelido = input('Coloque o seu identificador: ')

    if apelido not in dict_apelidos.keys():
        print(f'\nO apelido {apelido} não existe.\nVerifique se você escreveu de forma correta\n')
    else:
        print(f'\nVocê tem: --{sum(dict_apelidos[apelido])}-- centavos.')