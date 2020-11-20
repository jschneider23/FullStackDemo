from flask import Flask, render_template
from backend import stock_info, stock_chart, stock_movers, stock_options
import html_generator as hg

app = Flask(__name__)

@app.route("/")
def home():
    context = {"DJI": hg.htmlIndexCard("$DJI"),
               "SPXX": hg.htmlIndexCard("$SPX.X"),
               "COMPX": hg.htmlIndexCard("$COMPX")}
    return render_template("home.html", context = context)

@app.route("/options")
def options():
    return render_template("options.html")

@app.route("/movers")
def movers():
    return render_template("movers.html")

if __name__ == "__main__":
    app.run(debug = True)
