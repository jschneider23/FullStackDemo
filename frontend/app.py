from flask import Flask, render_template
from backend import stock_info, stock_chart, stock_movers, stock_options

app = Flask(__name__)

@app.route("/")
def home():
    data = stock_movers.getMovers("$DJI", "up", "percent")
    return render_template("home.html", data = data)

@app.route("/options")
def options():
    return render_template("options.html")

@app.route("/movers")
def movers():
    return render_template("movers.html")

if __name__ == "__main__":
    app.run(debug = True)
