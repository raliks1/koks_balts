import requests
import string


# q = requests.get("https://zenquotes.io/api/quotes").json()

# nr = 1
# header = ["Nr", "Citāta autos", "1.vārds", "Citāts"]
# tabula = []

# for ieraksts in q:
#     vardi = ieraksts["q"].split()
#     pedejais_vards = vardi[-1].strip(string.punctuation)
#     tabula.append([nr, ieraksts["a"],vardi[0],pedejais_vards, len(vardi), ieraksts["q"]])
#     nr += 1
#     if nr > 10:
#         break

# print(tabulate(tabula, headers=header, tablefmt="grid", maxcolwidths=[None, None, None, 30]))
import tkinter as tk

def mainit_tekstu():
    teksts.config(text="Sliņķi ir forši!",fg="blue", font=("Ariel", 20))
    logs1.config(bg="black")

logs1 = tk.Tk()
logs1.title("sliņķu logs")
logs1.geometry("400x200+20+20") 

teksts = tk.Label(logs1, text="Sveiciens sliņķiem!", font = ("Ariel", 16) )
teksts.pack(pady=20)

poga = tk.Button(logs1, text="Nospied mani!", command=mainit_tekstu)
poga.pack(pady=10)

logs1.mainloop()
