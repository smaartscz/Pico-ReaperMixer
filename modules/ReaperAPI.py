import aiohttp
import asyncio
import modules.colors as colors

class ReaperAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    async def _send_request(self, command):
        url = f"{self.base_url}/_/{command}"
        print(colors.yellow + f"Sending request to URL: {url}")
        try:
            async with self.session.get(url) as response:
                response.raise_for_status()
                text = await response.text()
                print(colors.green + f"Response received: {text}")
                return text
        except aiohttp.ClientError as e:
            print(f"Request to {url} failed: {e}")
            return None

    async def get_transport(self):
        return await self._send_request('TRANSPORT')

    async def get_track_info(self, index):
        return await self._send_request(f'TRACK/{index}')

    async def mute(self, index, value):
        return await self._send_request(f'SET/TRACK/{index}/MUTE/{value}')

    async def play(self):
        return await self._send_request('SET/TRANSPORT/PLAY')
    
    async def set_volume(self, index, value):
        return await self._send_request(f'SET/TRACK/{index}/VOL/{value}')
    
    async def stop(self):
        return await self._send_request('SET/TRANSPORT/STOP')

    async def close(self):
        await self.session.close()
