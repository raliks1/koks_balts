from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATU_FAILS = "dati.json"

def nolasit_datus():
    if not os.path.exists(DATU_FAILS):
        return []
    with open(DATU_FAILS, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])
def forma():
    if request.method == "POST":
        jauns_ieraksts = {
            "vards": request.form.get("vards"),
            "uzvards": request.form.get("uzvards"),
            "klase": request.form.get("klase"),
            "prieksmets": request.form.get("prieksmets"),
        }

        visi_dati = nolasit_datus()
        visi_dati.append(jauns_ieraksts)

        with open(DATU_FAILS, "w", encoding="utf-8") as f:
            json.dump(visi_dati, f, indent=4, ensure_ascii=False)

        return redirect(url_for("apskats"))

    return render_template("forma.html")

@app.route("/apskats")
def apskats():
    saraksts = nolasit_datus()
    return render_template("apskats.html", dati=saraksts)

if __name__ == "__main__":
    app.run(debug=True)