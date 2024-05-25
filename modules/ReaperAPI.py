import requests
import modules.colors as colors
class ReaperAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def _send_request(self, command):
        url = f"{self.base_url}/_/{command}"
        print(colors.yellow + f"Sending request to URL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(colors.green + f"Response received: {response.text}")
            return response.text
        except requests.RequestException as e:
            print(f"Request to {url} failed: {e}")
            return None

    def get_transport(self):
        return self._send_request('TRANSPORT')

    def get_track_info(self, index):
        return self._send_request(f'TRACK/{index}')

    def mute(self, index, value):
        return self._send_request(f'SET/TRACK/{index}/MUTE/{value}')

    def play(self):
        return self._send_request('SET/TRANSPORT/PLAY')

    def stop(self):
        return self._send_request('SET/TRANSPORT/STOP')
