from flask import Flask, render_template, request
from backend import stock_info, stock_chart, stock_movers, stock_options
import html_generator as hg
import flask

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    errorMsg = None
    context = {}
    if request.method == "POST":
        formInput = request.form["search"]
        modalScript = flask.Markup("""
            <script>
                $('#viewStock').modal('show');
                console.log($('#viewStock'))
            </script>
        """)
        modalTitle = formInput + " Title"
        modalBody = formInput + " Data would go here"
        context.update({"modalScript": modalScript, "modalTitle": modalTitle,
                        "modalBody": modalBody})
    tupDJI = hg.htmlIndexCard("$DJI")
    tupSPXX = hg.htmlIndexCard("$SPX.X")
    tupCOMPX = hg.htmlIndexCard("$COMPX")
    context.update({"clrDJI": tupDJI[0], "DJI": tupDJI[1], 
                    "clrSPXX": tupSPXX[0], "SPXX": tupSPXX[1],
                    "clrCOMPX": tupCOMPX[0], "COMPX": tupCOMPX[1]})
    print("Context: " + str(context))
    return render_template("home.html", context = context)

@app.route("/options")
def options():
    return render_template("options.html")

@app.route("/movers")
def movers():
    return render_template("movers.html")

if __name__ == "__main__":
    app.run(debug = True)
