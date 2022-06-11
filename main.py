import requests

base_url = 'https://api.duckduckgo.com'
parameters_dog_search = {'q': 'dogs', 'format': 'json', 'pretty': 1}
parameters_dogecoin_search = {'q': 'dogecoin', 'format': 'json', 'pretty': 1}
resp_dog = requests.get(base_url, parameters_dog_search)
resp_dogecoin = requests.get(base_url, parameters_dogecoin_search)
print(resp_dog.json().get('Image', 'there are no images for this instant Answer'))
print(resp_dogecoin.json().get('AbstractURL'))
