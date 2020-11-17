from flask import Flask, render_template
from backend import stock_info, stock_chart, stock_movers, stock_options

app = Flask(__name__)

@app.route("/")
def index():
    data = stock_movers.getMovers("$DJI", "up", "percent")
    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run(debug = True)
