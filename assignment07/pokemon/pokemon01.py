import aiofiles
import asyncio
import json

pokemonapi_directory = 'D:\\Project year3\\Team3.1\\Asynchronous program development\\THREADING\\asyncioclass67\\assignment07\\pokemon\\pokemonapi'
pokemonmove_directory = 'D:\\Project year3\\Team3.1\\Asynchronous program development\\THREADING\\asyncioclass67\\assignment07\\pokemon\\pokemonmove'

async def main():
    # Read the contents of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}\\articuno.json', mode='r') as f: contents = await f.read()
    print(contents)
    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    print(pokemon['name'])

asyncio.run(main())