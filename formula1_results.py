import json
import requests

# results
num_positions = 6
results_url = "https://ergast.com/api/f1/current/last/results.json"

res = requests.get(results_url)
res_json = json.loads(res.text)
data = res_json["MRData"]["RaceTable"]["Races"][0]

circuit = data["Circuit"]["circuitName"]
location = data["Circuit"]["Location"]["country"]
results = data["Results"]

print(f'\nRound {data["round"]}  {data["date"]}')
print(f'{circuit} ({location})\n')

for i in range(num_positions):
    driver = results[i]["Driver"]
    ctor = results[i]["Constructor"]["name"]
    print(f'p{results[i]["position"]} \t {ctor:<15} \t '
          f'{driver["givenName"]} {driver["familyName"]}')

# next race
next_race_url = "https://ergast.com/api/f1/current/next.json"

res = requests.get(next_race_url)
res_json = json.loads(res.text)
data = res_json["MRData"]["RaceTable"]["Races"][0]

print(f'\nNext race: {data["date"]} \t {data["raceName"]}\n')
