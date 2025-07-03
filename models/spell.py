import requests

def get_spells():
    req = requests.get('https://api.potterdb.com/v1/spells')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch spells: {req.status_code}")
    
def get_spell_by_id(spell_id):
    req = requests.get(f'https://api.potterdb.com/v1/spells/{spell_id}')
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch spell with ID {spell_id}: {req.status_code}")