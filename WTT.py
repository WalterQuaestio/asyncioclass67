import requests  # Synchronous HTTP requests to fetch the data
import aiofiles
import asyncio
import json
from datetime import datetime

def fetch_pokemon_data(url):
    response = requests.get(url)
    return response.json()

async def save_data_to_file(data, filename):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(data))

async def read_and_process_pokemon_data(filename, ability_name):
    async with aiofiles.open(filename, 'r') as file:
        content = await file.read()
        data = json.loads(content)
        pokemon_list = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        return pokemon_list

async def main():
    # Record the start time
    start_time = datetime.now()

    # Define URLs and filenames
    urls = {
        "battle_armor": "https://pokeapi.co/api/v2/ability/battle-armor",
        "speed_boost": "https://pokeapi.co/api/v2/ability/speed-boost"
    }
    filenames = {
        "battle_armor": "battle_armor.json",
        "speed_boost": "speed_boost.json"
    }

    # Fetch and save the data for each ability
    for ability, url in urls.items():
        data = fetch_pokemon_data(url)
        await save_data_to_file(data, filenames[ability])

    # Process and print the results with time display
    for ability, filename in filenames.items():
        pokemon_list = await read_and_process_pokemon_data(filename, ability)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time: {current_time}")
        print(f"Ability: {ability.replace('_', ' ').title()}")
        print(f"Number of Pokémon: {len(pokemon_list)}")
        print(f"Pokémon names: {', '.join(pokemon_list)}\n")

    # Record the end time
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Total Time Elapsed: {elapsed_time}")

# Run the event loop
asyncio.run(main())
