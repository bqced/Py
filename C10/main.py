import requests
import json

response = requests.get("https://v2.jokeapi.dev/joke/Any")
data = response.text
parse_json = json.loads(data)

joke = parse_json['setup']
answer = parse_json['delivery']
racist = parse_json['flags']['racist']
sexist = parse_json['flags']['sexist']

if racist:
  print("Thats inapropriate")
elif sexist:
  print('You are sexist')
else:
  print(joke)
  print(answer)
