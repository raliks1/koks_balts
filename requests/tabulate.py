import requests
from tabulate import tabulate

q = requests.get("https://zenquotes.io/api/quotes").json()

header = ["Citāta sutos", "Citāts"]
tabula = []

for ieraksts in q:
    tabula.append([ieraksts['a'], ieraksts['q']])  

print(tabulate(tabula, headers=header, tablefmt="grid"))

