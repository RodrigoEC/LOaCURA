import requests

url = 'http://lad.ufcg.edu.br/loac/uploads/OAC/anon.txt'
response = requests.get(url, allow_redirects=True)

with open('anon.txt', 'wb') as file:
    file.write(response.content)

with open('anon.txt', 'r') as file:
    dict_apelidos = {}
    for linha in file.readlines():
        [identificador, _, centavos, *descricao] = linha.split() 
        
        if identificador not in dict_apelidos:
            dict_apelidos[identificador] = []

        dict_apelidos[identificador].append(int(centavos))

    apelido = input('Coloque o seu identificador: ')

    print(f'Você tem: --{sum(dict_apelidos[apelido])}-- centavos.')