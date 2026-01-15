import requests

atbilde = requests.get("https://catfact.ninja/fact")
if atbilde.status_code == 200:
    dati = atbilde.json()
    print(f"Žināji, ka , {dati['fact']}")
else:
    print("Neizdevās iegūt datus no API")