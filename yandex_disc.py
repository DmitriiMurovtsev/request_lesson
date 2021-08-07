import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/'
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token}'
        }
        for name_file in file_path:
            r = requests.get(url + 'v1/disk/resources/upload/', headers=headers, params={'path': name_file})
            upload_url = r.json()['href']
            with open(name_file, 'rb') as file:
                requests.put(upload_url, headers=headers, files={'file': file})

if __name__ == '__main__':
    path_to_file = ['2.txt', '3.txt']
    token = ' '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)