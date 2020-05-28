import requests

def return_cep_data(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/unicode/".format(cep))
    print(response.status_code)
    print(response.json())
    cep_data = response.json()
    return cep_data

def return_poke_data(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon))
    print(response.status_code)
    print(response.json())
    poke_data = response.json()
    return poke_data

def return_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # return_cep_data('01001000')
    # return_poke_data('sylveon')
    # response = return_response("https://serenesforest.net")
    # print(response)
    pass