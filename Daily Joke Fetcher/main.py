import requests
response = requests.get("https://official-joke-api.appspot.com/jokes/random")
data = response.json()

print(data)
print(type(data))


print(data["setup"]+"😎")
print(data["punchline"]+"🤣😂")
#https://www.freepublicapis.com/official-joke-api