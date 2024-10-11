import requests
import random


base_url =  'https://pokeapi.co/api/v2/pokemon'
limit = 200
url=f"{base_url}?limit={limit}"


def fetch_pokemons_data():

    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
    else:
        print(f'Error: fetching data failed! {res.status_code}')

    pokemon_list = data['results']
    
    return pokemon_list



def fetch_single_pokemon_details(random_pokemon_name):

    res = requests.get(f'{base_url}/{random_pokemon_name}')
    if res.status_code == 200:
        data = res.json()
    else:
        print(f'Error: fetching data failed! {res.status_code}')
   
    pokemon_details_data = data

    # Pokemon types values 
    pokemon_type_names  = []
    for type in pokemon_details_data['types']:
        pokemon_type_names.append(type['type']['name'])

    
    # extract pokemon another values 
    # object to be appended
    pokemon_details = {
        "id": pokemon_details_data['id'],
        "name": pokemon_details_data['name'],
        "height": pokemon_details_data['height'],
        "weight": pokemon_details_data['weight'],
        "types": pokemon_type_names
    }

    return pokemon_details


      
def random_pokemon():

    pokemon_list = fetch_pokemons_data()

    # randomly select a Pokémon from the list
    random_pokemon = random.choice(pokemon_list)
    random_pokemon_name = random_pokemon['name']
    print('Random Pokemon was chosen.')

    # print(random_pokemon_name)
    return random_pokemon_name