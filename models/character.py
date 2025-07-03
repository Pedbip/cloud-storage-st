import requests

def get_characters():
    req = requests.get("https://api.potterdb.com/v1/characters")
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch characters: {req.status_code}")
    
def get_character_by_id(character_id):
    req = requests.get(f"https://api.potterdb.com/v1/characters/{character_id}")
    if req.status_code == 200:
        return req.json()
    else:
        raise Exception(f"Failed to fetch character with ID {character_id}: {req.status_code}")