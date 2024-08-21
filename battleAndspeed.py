import aiofiles
import asyncio
import json


url_battle-armor = 'https://pokeapi.co/api/v2/ability/battle-armor'
url_speed-boost  = 'https://pokeapi.co/api/v2/ability/speed-boost'



async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{url_battle-armor}\\articuno.json', mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    # Opoen a new file to write the lish of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves)) 
        

asyncio.run(main())