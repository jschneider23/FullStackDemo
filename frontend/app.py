from flask import Flask, render_template, request
from frontend import html_generation as hg
import flask

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    context = {"home": "active"}
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

@app.route("/options", methods = ["POST", "GET"])
def options():
    context = {"options": "active"}
    if request.method == "POST":
        sym = request.form["search"].strip().upper()
        conType = request.form["conType"]
        numStrikes = request.form["numStrikes"]
        strike = request.form["strike"]
        rng = request.form["range"]
        fromDate = request.form["fromDate"]
        toDate = request.form["toDate"]
        expMonth = request.form["expMonth"]
        standard = request.form["standard"]
        modal = hg.htmlOCModalData(sym, conType, numStrikes, strike, rng, fromDate, toDate, expMonth, standard)
        context.update({"modalScript": modal["script"],
                        "modalTitle": modal["title"],
                        "modalOptionChain": modal["oc"],
                        "errorMsg": modal["errorMsg"]})
    return render_template("options.html", context = context)

@app.route("/movers")
def movers():
    context = {
        "movers": "active",
        "DJIUpPercent": hg.htmlMoverCard("$DJI", "up", "percent"),
        "DJIUpValue": hg.htmlMoverCard("$DJI", "up", "value"),
        "DJIDownPercent": hg.htmlMoverCard("$DJI", "down", "percent"),
        "DJIDownValue": hg.htmlMoverCard("$DJI", "down", "value"),
        "SPXXUpPercent": hg.htmlMoverCard("$SPX.X", "up", "percent"),
        "SPXXUpValue": hg.htmlMoverCard("$SPX.X", "up", "value"),
        "SPXXDownPercent": hg.htmlMoverCard("$SPX.X", "down", "percent"),
        "SPXXDownValue": hg.htmlMoverCard("$SPX.X", "down", "value"),
        "COMPXUpPercent": hg.htmlMoverCard("$COMPX", "up", "percent"),
        "COMPXUpValue": hg.htmlMoverCard("$COMPX", "up", "value"),
        "COMPXDownPercent": hg.htmlMoverCard("$COMPX", "down", "percent"),
        "COMPXDownValue": hg.htmlMoverCard("$COMPX", "down", "value")
    }
    return render_template("movers.html", context = context)

if __name__ == "__main__":
    app.run(debug = True)
