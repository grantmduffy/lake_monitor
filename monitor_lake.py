import requests
import rtsp
from pathlib import Path
from datetime import datetime
from time import sleep
import json
from tqdm import tqdm

with open('private.txt', 'r') as f:
    api_key, rtsp_url, data_path = (x.strip() for x in f.readlines())


def capture(
        data_path=Path(data_path),
        api_key=api_key,
        lat=48.134143, lon=-122.3029389,
):
    if not data_path.is_dir():
        data_path.mkdir()
    client = rtsp.Client(rtsp_server_uri=rtsp_url, verbose=False)
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
    for i in tqdm(range(10)):
        capture()
        sleep(3)
