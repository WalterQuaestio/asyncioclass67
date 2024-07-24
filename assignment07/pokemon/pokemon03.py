import aiofiles
import asyncio
import json

pokemonapi_directory = 'D:\\Project year3\\Team3.1\\Asynchronous program development\\THREADING\\asyncioclass67\\assignment07\\pokemon\\pokemonapi'
pokemonmove_directory = 'D:\\Project year3\\Team3.1\\Asynchronous program development\\THREADING\\asyncioclass67\\assignment07\\pokemon\\pokemonmove'

async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}\\articuno.json', mode='r') as f:
        contents = await f.read()
    
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]

    # Opoen a new file to write the lish of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves)) 
        

asyncio.run(main())