import requests
import rtsp
from pathlib import Path
from datetime import datetime
from time import sleep
import json

with open('api_key.txt', 'r') as f:
    api_key = f.read()


def capture(
        data_path=Path('data'),
        api_key=api_key,
        lat=48.134143, lon=-122.3029389
):
    client = rtsp.Client(rtsp_server_uri='rtsp://grant:pswd4wyse@192.168.86.29/live', verbose=False)
    img = None
    while img is None:
        img = client.read()
    client.close()
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')

    datetime_str = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    img.save(data_path / (datetime_str + '.png'))
    with open(data_path / (datetime_str + '.json'), 'w') as f:
        json.dump(r.text, f)


if __name__ == '__main__':
    for i in range(10):
        capture()
        sleep(3)
