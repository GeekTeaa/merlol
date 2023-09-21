import json
import requests
import sys
from pathlib import Path
# import cv2

def hello_world():
    return "Hello World!"

class DataDragon():
    def __init__(self, path=Path('../data-dragon/')):
        self._path = path
        self._version = self._get_current_version()
        self._live_version = self._get_live_version()

    @property
    def champions(self):
        path = self._path / self._version / 'data' / 'en_US' / 'champion.json'
        class Champions():
            def _champ_json(self, champ_file):
                return json.load(champ_file)["data"]

            def __getitem__(self, champ : str):
                if (path.exists()):
                    with open(path.absolute()) as champ_file:
                        return self._champ_json(champ_file)[champ]

            def __getitem__(self, champ_id : int):
                if (path.exists()):
                    with open(path.absolute()) as champ_file:
                        for champion, data in self._champ_json(champ_file).items():
                            if data["key"] == f'{champ_id}':
                                return data

        return Champions()

    @property
    def items(self):
        path = self._path / self._version / 'data' / 'en_US' / 'item.json'
        if (path.exists()):
            with open(path.absolute()) as champ_file:
                return json.load(champ_file)["data"]
        return None

    @property
    def images(self):
        dd_path = self._path
        version = self._version
        class Images:
            def __getitem__(self, champ : str):
                path = dd_path / version / 'img' / 'champion' / f'{champ}.png'
                return str(path.absolute())

        return Images()

    @property
    def version(self):
        return self._version

    @property
    def live_version(self):
        return self._live_version

    def _get_live_version(self):
        response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
        if response.status_code != 200: return None

        return response.json()[0]

    def _get_current_version(self):
        if not self._path.exists(): return None
        if not self._path / '13.18.1' : return None
        return '13.18.1'

if __name__ == "__main__":
    dd = DataDragon()

    # print(json.dumps(dd.champions["Ezreal"], indent=2))
    # print(json.dumps(dd.items["1001"], indent=2))

# champ_name = dd.champions[81]["name"]
# img = cv2.imread(dd.images[champ_name], cv2.IMREAD_ANYCOLOR)
# while True:
#     cv2.imshow("Ezreal", img)
#     cv2.waitKey(0)
#     sys.exit()
#
# cv2.destroyAllWindows()
