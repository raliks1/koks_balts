import os
os.system('cls') #attira terminala logu pasa sakuma
print("\n") # ieliek tuksu rindinu pirms izdrukas

import requests
from bs4 import BeautifulSoup
from plyer import notification

url = "https://www.timeanddate.com/worldclock/japan/tokyo"

def get_Time_data(url):
    try:
       r = requests.get(url, timeout=10)
       r.raise_for_status()
       return r.text
    except requests.exceptions.RequestException as e:
        print(f"Kļūda: {e}")
        return None
    
htmldata = get_Time_data(url)

if htmldata:
    soup = BeautifulSoup(htmldata, "html.parser")
    time_elem = soup.find("span", id="ct")
    date_elem = soup.find("span", id="ctdat")
    laiks = time_elem.text if time_elem else "Nav datu"
    datums = date_elem.text if date_elem else "Nav datu"
    result = f"Pašreizējais laiks japānā: {laiks}\nDatums: {datums}"
    notification.notify(
        title = "Sveiks ralik! Laiks un Datums Japānā ir:",
        message = result, 
        timeout = 10
    )
else:
    notification.notify(
        title="Kļūda!",
        message = "Nekas nav zināms",
        timeout = 10
    )