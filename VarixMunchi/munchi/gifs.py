
import aiohttp
import json
import random
from requests import HTTPError
from config import Config

config = Config()
guilds = config.guilds


async def random_gif(q, limit=10, rating='pg-13'):
    """Get a random gif with the specified search query from GIPHY (requires valid API key)"""
    if not q:
        return

    search_url = f'https://api.giphy.com/v1/gifs/search?q={q.replace(" ", "+")}&api_key={config.giphy_token}&limit={limit}&rating={rating}'

    async with aiohttp.ClientSession() as session:
        async with await session.get(search_url) as resp:
            if resp.status != 200:
                raise HTTPError(resp.status)

            data = json.loads(await resp.text())

    random_choice = random.randint(0, len(data['data']))

    return data['data'][random_choice]['images']['original']['url']
