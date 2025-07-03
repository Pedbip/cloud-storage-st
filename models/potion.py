import requests

def get_potions():
    req = requests.get('https://api.potterdb.com/v1/potions')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch potions: {req.status_code}")
    
def get_potion_by_id(potion_id):
    req = requests.get(f'https://api.potterdb.com/v1/potions/{potion_id}')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch potion with ID {potion_id}: {req.status_code}")