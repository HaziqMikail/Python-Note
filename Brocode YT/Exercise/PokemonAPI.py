import requests  # !pip install requests to install requests library for making API calls

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Pokémon not found. Please check the name and try again.")
        return

pokemon_name = input("Enter the name of a Pokémon: ").lower()
pokemon_info = get_pokemon_data(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].title()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print("Types:")
    for poke_type in pokemon_info['types']:
        print(f" - {poke_type['type']['name'].title()}")
else:
    print("No data available.")









