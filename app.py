# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


# app = Flask(__name__)
# from flask import Flask, render_template, request, redirect, url_for
# @app.route("???")
# request.args.get("???")
# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"
# render_template("???", ???, ???)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import json

app = Flask(__name__)
json = "/data/recenze.json"
message = {}

def save_data():
    with open (recenze.json, "w", encoding="UTF-8") as f:
        json.dump(message, f, indent=4)

@app.route("/")
def vitej():
    return render_template("vitej.html")

@app.route("/")
def form():
    login = request.args.get("login")
    zprava = request.args.get("text")
    if zprava == "nic":
        odpoved = "nic"
        print("uživatel byl příliš líný na napsání recenze") 
    else: print ("text")
    return render_template ("form.html")
        

if __name__ == "__main__": app.run(debug=True) # Zajišťuje, že aplikace se spustí jen když je otevřena přímo a ne importovaná jinam