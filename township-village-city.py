import requests
import json

subscription_key = 'your-subscription-key'
address = '51039 O R AND W STATION ST, JACOBSBURG OH 43933'

url = f'https://atlas.microsoft.com/search/address/json?subscription-key={subscription_key}&api-version=1.0&query={address}'

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    if len(data['results']) > 0:
        result = data['results'][0]
        city = result['address']['municipality']
        township = result['address'].get('township')
        village = result['address'].get('village')
        print(f"City: {city}, Township: {township}, Village: {village}")
    else:
        print("Address not found.")
else:
    print("Error:", response.status_code, response.text)
