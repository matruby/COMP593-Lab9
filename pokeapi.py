
import requests as req

def fetch_poke_info(poke_name):
    """
    Retrieves Pokemon Information
    """
    # Clean up the Pokemon input
    clean_name = poke_name.strip()
    clean_name = clean_name.lower()

    # Check the API for that pokemon
    poke_info = req.get(f'https://pokeapi.co/api/v2/pokemon/{clean_name}')
    # Check if the reponse succeded
    if poke_info.status_code == req.codes.ok:
        print('Success')
        poke_dict = poke_info.json()
        return poke_dict


poke_info = fetch_poke_info('applin')
# Pokemon types 
poke_types = poke_info['types']

types = [poke['type']['name'] for poke in poke_types]

if len(types) == 1:
    print(types[0])
else:
    print(', '.join(types))

