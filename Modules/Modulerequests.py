import requests
import json

r = requests.get(url='https://api.github.com/events', params=None, data= None, headers=None, timeout=None, cookies=None)  # send your cookies with cookies

r2 = json.loads(r.text)

print(r2[0]["actor"]["id"])


# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # post with requests
# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

print(r.text[:50])

# passing some data to URL's query string to get personalised results based on the data
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

# getting non-text data from the url- as binary

print(r.content[:10])  # .content returns the data in binary

r2 = requests.get("https://en.wikipedia.org/wiki/Virat_Kohli")
# print(r2)

"""from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r2.content))"""

