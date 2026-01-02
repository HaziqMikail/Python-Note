import requests  # !pip install requests to install requests library for making API calls

base_url = "https://pokeapi.co/api/v2/"  #? Base URL for the Pokémon API website


#TODO: Create a function to get Pokémon data by name
def get_pokemon_data(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"  #? Construct the full API endpoint URL
    response = requests.get(url)                #? Make a GET request to the API

    if response.status_code == 200:             #? Check if the request was successful
        pokemon_data = response.json()          #? get the JSON response data
        return pokemon_data                     #? Return the Pokémon data
    else:
        print("Pokémon not found. Please check the name and try again.")
        return

#TODO - Get user input for Pokémon name
pokemon_name = input("Enter the name of a Pokémon: ").lower()  
pokemon_info = get_pokemon_data(pokemon_name)                   #? Fetch data for the specified Pokémon

#TODO - Display relevant Pokémon information
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









