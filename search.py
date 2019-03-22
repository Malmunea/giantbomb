import requests

''' READAPI Key from text file '''
with open("apikey","r") as file:
    APIKEY = file.readline().rstrip("\n")
print("API Key: "+APIKEY)

user_input = input("Enter game name: ")

url = "https://www.giantbomb.com/api/search/?query="+user_input+"&format=json&api_key="+APIKEY
headers = {
  'User-Agent':'testscript',
  'From': 'black-2-blue@hotmail.com'
}

response = requests.get(url,headers=headers)

for game in response.json()["results"]:
    print("Name: {}\tguid: {}".format(game["name"],game["guid"]))
