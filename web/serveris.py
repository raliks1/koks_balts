from flask import Flask

app = Flask(__name__)


@app.route('/')

def sakums():
    return """<body style=background-color:blue;>
<h1 style=color:yellow; style=;>Sveika gudrā 11.a klase!</h1><p>Šis ir mūsu lielākais sasniegums!</p>
</body>"""
@app.route('/otrais')
def otraijs(): return """<body>
<h1 style=color:green; style=;>Šī ir otrā lapa!</h1><p>Es to atceros!!</p> 
</body>"""
@app.route('/hobijs')

def hobijs(): 
    hobijs = "Gym"
    return f"""<body>
<h1 style=color:black; style=;>Mans hobijs ir {hobijs}</h1><p>es to spēju!</p> 
</body>"""
if __name__ == '__main__':
    app.run(debug=True)
