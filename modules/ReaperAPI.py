#import urequests
import requests as urequests
import modules.colors as colors

class ReaperAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    async def _send_request(self, command):
        url = f"{self.base_url}/_/{command}"
        print(colors.yellow + f"Sending request to URL: {url}" + colors.reset)
        try:
            response = urequests.get(url)
            if response.status_code == 200:
                text = response.text
                print(colors.green + f"Response received: {text}" + colors.reset)
                response.close()
                return text
            else:
                print(colors.red + f"Request to {url} failed with status code {response.status_code}" + colors.reset)
                response.close()
                return None
        except Exception as e:
            print(colors.red + f"Request to {url} failed: {e}" + colors.reset)
            return None

    async def get_transport(self):
        return await self._send_request('TRANSPORT')

    async def get_track_info(self, index):
        return await self._send_request(f'TRACK/{index}')
    
    async def get_tracks(self):
        return await self._send_request('NTRACK')
    
    async def mute(self, index, value):
        return await self._send_request(f'SET/TRACK/{index}/MUTE/{value}')

    async def play(self):
        return await self._send_request('SET/TRANSPORT/PLAY')
    
    async def set_volume(self, index, value):
        return await self._send_request(f'SET/TRACK/{index}/VOL/{value}')
    
    async def stop(self):
        return await self._send_request('SET/TRANSPORT/STOP')

    async def close(self):
        # No session management needed with urequests, so this is a no-op
        pass