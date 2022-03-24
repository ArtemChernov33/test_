import requests


tokenYD = "AQAAAAAJQVzgAADLWxS59s2yPEi3kvhpYX9CVn4"

url = 'https://cloud-api.yandex.net/v1/disk/resources/'
url_z = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


path = "qwqz"
def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': f'OAuth {tokenYD}'}
    create_dir = requests.api.put(url, headers=headers, params=params)
    #return create_dir.text
    return create_dir.status_code



