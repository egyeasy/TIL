import requests

response = requests.get('https://last-pang-egyeasy.c9users.io/api/v1/musics/')
print(response.json())