from flask import Flask, render_template, request
from backend import stock_info, stock_chart, stock_movers, stock_options
import html_generator as hg
import flask

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    context = {}
    if request.method == "POST":
        formInput = request.form["search"].strip().upper()
        modal = hg.htmlModalData(formInput)
        if modal is None:
            formInput = formInput.capitalize()
            nameResults = hg.htmlNameResults(formInput)
            if nameResults is not None:
                context["nameResults"] = nameResults
            else:
                errorMsg = f"""
                    \"<i>{formInput.upper()}</i>\" doesn't exist as a valid
                    symbol, name, or name fragment matching a symbol in TD's
                    Database.  Please enter a valid symbol, name, or name
                    fragment.
                """
                context["errorMsg"] = flask.Markup(errorMsg)
        else:
            context.update({"modalScript": modal["script"], 
                            "modalTitle": modal["title"],
                            "modalQuote": modal["quote"],
                            "modalChart": modal["chart"],
                            "modalInfo": modal["info"]})
    tupDJI = hg.htmlIndexCard("$DJI")
    tupSPXX = hg.htmlIndexCard("$SPX.X")
    tupCOMPX = hg.htmlIndexCard("$COMPX")
    context.update({"clrDJI": tupDJI[0], "DJI": tupDJI[1], 
                    "clrSPXX": tupSPXX[0], "SPXX": tupSPXX[1],
                    "clrCOMPX": tupCOMPX[0], "COMPX": tupCOMPX[1]})
    return render_template("home.html", context = context)

@app.route("/options")
def options():
    return render_template("options.html")

@app.route("/movers")
def movers():
    return render_template("movers.html")

if __name__ == "__main__":
    app.run(debug = True)
