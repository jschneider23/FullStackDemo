# This file contains all functions that have @app.route decorater, which
# provide the main functionality for the server at various request urls.

from flask import Flask, render_template, request
from frontend import html_generation as hg, app_aux as aux
from backend import stock_chart as sc
import flask
import os

# Required to initialize Flask App.
app = Flask(__name__)

# Renders the Home page accordingly, depending on whether a GET request is
# sent (when opening the app for the first time or navigating to the root url)
# or a POST request is sent (submitting the Stock Quote & Information Lookup
# Form).  Handles all of the various form cases and renders this information
# to the user with the modal loading functionality using the same html
# generation function as the modal loading on the Movers page.
@app.route("/", methods = ["POST", "GET"])
def home():
    context = {"home": "active"}
    aux.clearOldGraphs()
    if request.method == "POST":
        formInput = request.form["search"].strip().upper()
        #THIS CAN BE OPTIMIZED TODO
        modal = hg.htmlModalData(formInput)
        if modal is None:
            formInput = formInput.capitalize()
            nameResults = hg.htmlNameResults(formInput)
            if isinstance(nameResults, dict):
                modal = hg.htmlModalData(nameResults["direct"])
                context.update({"modalScript": modal["script"], 
                                "modalTitle": modal["title"],
                                "modalQuote": modal["quote"],
                                "modalInfo": modal["info"]})
            elif nameResults is not None:
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
                            "modalInfo": modal["info"]})
    cardDJI = hg.htmlIndexCard("$DJI")
    cardSPXX = hg.htmlIndexCard("$SPX.X")
    cardCOMPX = hg.htmlIndexCard("$COMPX")
    context.update({"cardDJI": cardDJI,
                    "cardSPXX": cardSPXX,
                    "cardCOMPX": cardCOMPX})
    return render_template("home.html", context = context)

# Creates a stock or index chart on the backend and writes the html to the file
# at the destination shown below with the given parameters: a stock or index
# symbol, a time setting string (ex. 5d, 3m, 1y, etc.), and a true or false
# value as a string for whether or not to include extended hours data.  This
# html is copied and returned as wrapped, valid html, and displayed in a modal
# using a jQuery load function.
@app.route("/graph/<sym>/<time>/<hasExtHrs>")
def showGraph(sym, time, hasExtHrs):
    aux.clearOldGraphs()
    sc.createGraph(sym, time = time, hasExtHrs = hasExtHrs)
    file = open(f"frontend/graphs/graph{sym}{time}{hasExtHrs}.html")
    contents = file.read()
    file.close()
    return flask.Markup(contents)

# Provides a url destination for the server to return new Index Card html.
# Since the color of each card needs to be defined in the class of the card
# element, a new card is returned by each call to this function, which then
# replaces the old card.
@app.route("/refresh/<strippedIndexSym>")
def refreshIndexCard(strippedIndexSym):
    if strippedIndexSym == "DJI":
        indexSym = "$DJI"
    elif strippedIndexSym == "SPXX":
        indexSym = "$SPX.X"
    else:
        indexSym = "$COMPX"
    return hg.htmlIndexCard(indexSym)

# Renders the Options page accordingly, depending on whether a GET request is
# sent (when navigating to the Options page url directly or clicking the nav
# link) or a POST request is sent (after submitting the Options Chain form).
# Handles all of the various form cases and displays the appropriate response
# to the user, as well as handling empty and disabled fields on the server
# before sending parameters to the backend for processing and API retrieval.
@app.route("/options", methods = ["POST", "GET"])
def options():
    context = {"options": "active"}
    if request.method == "POST":
        sym = request.form["search"].strip().upper()
        conType = request.form["conType"]
        numStrikes = request.form.get("numStrikes", "")
        strike = request.form.get("strike", "")
        rng = request.form["range"]
        fromDate = request.form.get("fromDate", "")
        toDate = request.form.get("toDate", "")
        expMonth = request.form.get("expMonth", "ALL")
        standard = request.form["standard"]
        modal = hg.htmlOCModalData(sym, conType, numStrikes, strike, rng,
                                   fromDate, toDate, expMonth, standard)
        context.update({"modalScript": modal.get("script"),
                        "modalTitle": modal.get("title"),
                        "modalOptionChain": modal.get("oc"),
                        "errorMsg": modal.get("errorMsg", "")})
    return render_template("options.html", context = context)

# Loads gainer and loser movers tables for each of the API supported indicies
# ranked by both percentage and value, displaying the ranked by percentage
# tables by default and having the ranked by value tables preloaded so a simple
# toggle button can be used to nearly instantly show the other tables for each
# card.  While this does result in slower initial page load times, it allows
# for a more seamless experience after loading instead of using jQuery load
# calls.
@app.route("/movers")
def movers():
    aux.clearOldGraphs()
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

# This function loads a Stock/Index Quote & Information Profile from a link
# on either the Home Page Search by Name Results Table or a Movers Card.  It
# also hypothetically would allow for easy implementation on other additional
# pages if they were added and required this functionality.  This allows
# profiles to be viewed within the same page they were loaded from so an
# entire new page doesn't need to be loaded.
@app.route("/modalContent/<sym>")
def loadModalContent(sym):
    return hg.htmlModalContent(sym)

# Required for Flask App to run.
if __name__ == "__main__":
    app.run(debug = True)
