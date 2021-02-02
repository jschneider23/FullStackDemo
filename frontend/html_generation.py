# This file contains a large majority of the interaction with the backend in
# order to request API data formatted by the backend and then process this
# data to create various formatted html for various app functionality elements
# across all three pages.  In order for Flask to use a string of html as
# valid html (and not just a raw string), it is returned as wrapped Flask
# Markup, which lets Flask know that the html is valid and safe.  For the
# function comments below, any time html is mentioned it is referring to this
# valid, flask Markup wrapper object.

import json
import flask
import pandas as pd
from backend import bd_config as cfg, stock_info as si, stock_chart as sc, stock_movers as sm, stock_options as so
from frontend import fr_objects as fro
from datetime import datetime as dt, date
from dateutil.relativedelta import relativedelta as rd

# For added details on the purpose and functionality of this module, see the
# README

# *** Home Page *** #

# Given an index symbol (either "$DJI", "$SPX.X", or "$COMPX"), this function
# will produce and return an "At a Glance..." Bootstrap "Index" Card that
# is used to render the initial card present when loading the homepage as well
# as auto-refreshing every five seconds using jQuery load().  This uses the
# stock_info module's getBySymbol() function, with a special "indexCard"
# setting to only fetch the necessary attributes for the card.
def htmlIndexCard(indexSym):
    data = si.getBySymbol(indexSym, "indexCard")
    if "-" in str(data["netChange"]):
        cardClr = "bg-danger"
        arrow = "↓"
    elif data["netPercentChangeInDouble"] == "0.00%":
        cardClr = "bg-secondary"
        arrow = "↔"
    else:
        cardClr = "bg-success"
        arrow = "↑"
    cardText = f"""
        <div class="row">
            <div class="col"><b><u>Last:</u></b><br>
                {data["lastPrice"]}
            </div>
            <div class="col"><b><u>Close:</u></b><br>
                {data["closePrice"]}
            </div>
            <div class="col"><b><u>Value Chg:</u></b><br>
                {arrow} {data["netChange"]}
            </div>
            <div class="col"><b><u>% Chg:</u></b><br>
                {arrow} {data["netPercentChangeInDouble"]}
            </div>
        </div>
    """
    html = f"""
        <div class="card {cardClr} text-white shadow-sm">
            <h5 class="card-header">{indexSym}</h5>
            <div class-"card-body"><br>
                <h4 class="card-title">{data["cardTitle"]}</h4>
                <p class="card-text">{cardText}</p>
            </div>
        </div>
    """
    return flask.Markup(html)

# Produces and returns the html from the backend call to getBySymbol() rendered
# in the popup modal rendered after submitting a POST request, which is done
# through submitting the lookup form.  There will be slight variance in
# appearance depending on whether the symbol represents a stock or an index,
# such as in the title and chart axis labels.  If the backend returns None,
# however, then this function will return None.  This means that either sym
# is not a symbol and is a name search OR the symbol is not valid (both cases
# handled by app.py).
def htmlModalData(sym):
    if "$" in sym:
        symData = si.getBySymbol(sym, "indexFull")
        title = f"{sym} Index Quote &amp; Information"
    else:
        symData = si.getBySymbol(sym)
        title = f"{sym} Stock Quote &amp; Information"

    if symData is None:
        return None

    if "-" in str(symData["netChange"]):
        cardClr = "bg-danger"
        arrow = "↓" 
    elif symData["netPercentChangeInDouble"] == "0.00%":
        cardClr = "bg-secondary"
        arrow = "↔"
    else:
        cardClr = "bg-success"
        arrow = "↑"
    if len(symData["description"]) > 57:
        name = str(symData["description"])
        nameDisplay = f"{name[:54]}..."
    else:
        nameDisplay = symData["description"]
    quote = f"""
        <div class="card {cardClr} text-white">
            <div class="card-body">
                <h4>{sym}: {nameDisplay}</h4>
                <h6>
                    {arrow} {symData["netChange"]}
                    ({symData["netPercentChangeInDouble"]})
                </h6>
            </div>
        </div>
    """
    rows = ""
    for attr in symData:
        rows += f"""
            <tr>
                <th>{cfg.engAttrs[attr]}</th>
                <td>{symData[attr]}</td>
            </tr>
        """
    info = f"""
        <table id="table" class="table table-hover">
            <thead class="thead-light text-center">
                <tr>
                    <th colspan="2">{sym} Profile</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    """
    script = f"""
        $('#viewStock').modal('show');
        $(function() {{
            $('#chartCard').load('/graph/{sym}/10d/True');
        }})
        window.onload = function() {{
            document.getElementById("1dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/True');
            }}
            document.getElementById("3dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/True')
            }}

            document.getElementById("5dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/True')
            }}

            document.getElementById("10dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/True')
            }}

            document.getElementById("1mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/True')
            }}

            document.getElementById("3mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/True')
            }}

            document.getElementById("6mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/True')
            }}

            document.getElementById("1ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/True')
            }}

            document.getElementById("3ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/True')
            }}

            document.getElementById("5ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/True')
            }}

            document.getElementById("YTDtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/True')
            }}

            document.getElementById("1dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/False');
            }}

            document.getElementById("3dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/False')
            }}

            document.getElementById("5dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/False')
            }}

            document.getElementById("10dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/False')
            }}

            document.getElementById("1mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/False')
            }}

            document.getElementById("3mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/False')
            }}

            document.getElementById("6mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/False')
            }}

            document.getElementById("1yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/False')
            }}

            document.getElementById("3yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/False')
            }}

            document.getElementById("5yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/False')
            }}

            document.getElementById("YTDfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/False')
            }}
        }}
    """
    return {"script": flask.Markup(script),
            "title": flask.Markup(title),
            "quote": flask.Markup(quote),
            "info": flask.Markup(info)}

# Produces and returns the html that should be displayed after a name or name
# fragment search.  In most cases, this will be a Bootstrap card with a title
# showing the name searched for and number of results out 50 Max Accessible
# Results (TD Ameritrade's website obscures the ability to automate multiple
# result page navigation with the way the've constructed their pages) and then
# a table with the results containing a symbol link to open a modal.  If no
# results are found, then None is returned.  The rarest case is a direct match,
# which is when TD Ameritrade's website returns a direct match to a symbol, in
# which case no dataframe is returned and is instead a json object.
def htmlNameResults(name):
    dfResults = si.getByName(name)
    if dfResults is None:
        return None
    elif not isinstance(dfResults, pd.DataFrame):
        return {"direct": dfResults["symbol"]}
    else:
        rows = ""
        onclickScript = ""
        for ind in dfResults.index:
            sym = dfResults["Symbol"][ind]
            rows += f"""
                <tr>
                    <td>
                        <a id="{sym}sym" data-toggle="modal" href="#homeResultModal">
                            {sym}
                        </a>
                    </td>
                    <td>{dfResults["Company Name"][ind]}</td>
                    <td>{dfResults["Type"][ind]}</td>
                    <td>{dfResults["Exchange"][ind]}</td>
                </tr>
            """
            onclickScript += f"""
                document.getElementById("{sym}sym").onclick = function() {{
                    $('#modalContent').load('/modalContent/{sym}')
                }}
            """

        html = f"""
            <div class="card bg-light">
                <h3 class="text-center card-header">
                    Name Search For \"<i>{name}</i>\" Returned <i>
                    {len(dfResults)} Out of 50 Max Accessible Results</i>
                </h3>
                <table class="table table-responsive table-hover">
                    <thead class="thead-light">
                        <tr>
                            <th>Symbol</th>
                            <th>Name</th>
                            <th>Type</th>
                            <th>Exchange</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
                <script>
                    {onclickScript}
                </script>
            </div>
        """
    return flask.Markup(html)

# *** Options Page *** #

# Given parameters required for the TD Amertirade Options Chain API, this
# will produce the html for the contents of the Options Page modal that
# loads after form submission.  This return is either a dictionary containing
# the various parts that the template renders or just a dictionary containing
# an error message, which is sent to the template if a Key Error occurs in
# the try block.  This means the API could not find an options chain for
# the given the symbol or had another type of error.
def htmlOCModalData(sym, conType, numStrikes, strike, rng, expFrom, expTo,
                    expMonth, standard):
    try:
        ocDict = so.getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)
        underlyingPrice = ocDict["underlyingPrice"]
        dfCalls = ocDict.get("dfCalls")
        dfPuts = ocDict.get("dfPuts")
    except:
        errorMsg = f"""
            There was an error finding an Option Chain for \"<i>{sym}</i>\" 
            with the given filters.  Either \"<i>{sym}</i>\" is a
            non-optionable symbol or invalid parameters were provided.
        """
        return {"errorMsg": flask.Markup(errorMsg)}

    if dfCalls is not None and dfPuts is None:
        longerLen = len(dfCalls)
    elif dfPuts is not None and dfCalls is None:
        longerLen = len(dfPuts)
    else:
        longerLen = len(dfCalls) if len(dfCalls) > len(dfPuts) else len(dfPuts)

    callList = []
    putList = []
    oldExpDate = None
    newExpDate = None
    expDateGroups = []
    for ind in range(longerLen):
        if dfCalls is not None and dfPuts is None:
            if ind < len(dfCalls):
                row = dfCalls.loc[ind]
                newExpDate = row["Expiration"]
                if oldExpDate is None or oldExpDate == newExpDate:
                    call = fro.Option.fromRow(ind, underlyingPrice, row)
                    callList.append(call)
                    oldExpDate = newExpDate
                else:
                    edg = fro.OptionEDG.fromOptionLists(callList = callList)
                    expDateGroups.append(edg)
                    callList = []
                    oldExpDate = None
        elif dfPuts is not None and dfCalls is None:
            if ind < len(dfPuts):
                row = dfPuts.loc[ind]
                newExpDate = row["Expiration"]
                if oldExpDate is None or oldExpDate == newExpDate:
                    put = fro.Option.fromRow(ind, underlyingPrice, row)
                    putList.append(put)
                    oldExpDate = newExpDate
                else:
                    edg = fro.OptionEDG.fromOptionLists(putList = putList)
                    expDateGroups.append(edg)
                    putList = []
                    oldExpDate = None
        else:
            if ind < len(dfCalls):
                callRow = dfCalls.loc[ind]
            if ind < len(dfPuts):
                putRow = dfPuts.loc[ind]
                newExpDate = callRow["Expiration"]
            if oldExpDate is None or oldExpDate == newExpDate:
                call = fro.Option.fromRow(ind, underlyingPrice, callRow)
                put = fro.Option.fromRow(ind, underlyingPrice, putRow)
                callList.append(call)
                putList.append(put)
                oldExpDate = newExpDate
            else:
                edg = fro.OptionEDG.fromOptionLists(callList = callList, putList = putList)
                expDateGroups.append(edg)
                callList = []
                putList = []
                oldExpDate = None
    oc = fro.OptionChain(sym, round(float(underlyingPrice), 2), expDateGroups)
    htmlDict = oc.htmlOCAccordian()
    return {"script": flask.Markup(htmlDict["script"]),
            "title": flask.Markup(htmlDict["title"]),
            "oc": flask.Markup(htmlDict["oc"])}

# *** Movers Page *** #

# Generates the html for the contents of one of the six blank Movers cards
# already present on the Movers' page.  Each of the Dow Jones, S&P 500, and
# NASDAQ Composite have a Top Ten Gainers and Top Ten Losers Card, and
# displays one of two tables: top movers by % change or top movers by $ change.
# If there are less than 10 movers in a direction or the markets were closed
# during the day, appropriate placeholders are present in the table instead.
def htmlMoverCard(indexSym, direction, change):
    dfMovers = sm.getMovers(indexSym, direction, change)
    rows = ""
    onclickScript = ""
    ind = None
    tag = "percent" if change == "percent" else "value"
    for ind in dfMovers.index:
        sym = dfMovers["symbol"][ind]
        name = dfMovers["name"][ind]
        rows += f"""
            <tr class="text-white">
                <th>{int(ind)+1}</th>
                <td>
                <a id="{sym}sym{tag}" class="text-decoration-none text-white" data-toggle="modal" href="#moverModal">
                    {sym}
                </a>
                </td>
                <td>
                <a id="{sym}name{tag}" class="text-decoration-none text-white" data-toggle="modal" href="#moverModal">
                    {name}
                </a>
                </td>
                <td>{dfMovers["change"][ind]}</td>
                <td>{dfMovers["last"][ind]}</td>
            </tr>
        """
        onclickScript += f"""
            document.getElementById("{sym}sym{tag}").onclick = function() {{
                $('#modalContent').load('/modalContent/{sym}')
            }}

            document.getElementById("{sym}name{tag}").onclick = document.getElementById("{sym}sym{tag}").onclick
        """
    if ind is not None and ind < 9:
        ind += 1
        for ind in range(ind, 10):
            rows += f"""
                <tr class="text-white">
                    <td>{int(ind)+1}</td>
                    <td colspan="4">
                        N/A: Less than 10 movers of this type
                    </td>
                </tr>
            """
    if ind is None:
        for rank in range(1, 11):
            rows += f"""
                <tr class="text-white">
                    <td>{rank}</td>
                    <td colspan="4">MARKETS CLOSED TODAY</td>
                </tr>
            """
    html = f"""
        <div class="table-responsive">
            <table class="table table-hover table-borderless table-sm">
                <thead>
                    <tr class="text-white">
                        <th>Rank</th>
                        <th>Symbol</th>
                        <th>Name</th>
                        <th>Change</th>
                        <th>Last</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
        <script>
            {onclickScript}
        </script>
    """
    return flask.Markup(html)


# *** Home and Movers Page *** #

# This function is used to render an entire modal and associated modal script
# when clicking a symbol link on either the Home Page from Name Search Results
# or from the Movers Page via a mover from a Mover Card.
def htmlModalContent(sym):
    symData = si.getBySymbol(sym)
    if symData is None:
        return flask.Markup("""
            <div style="padding: 5px">
                <button type="button" class="close text-right" data-dismiss="modal">
                    &times;
                </button>
                <p>
                    API ERROR: TD Ameritrade identifies this symbol as real and
                    existing in their database, but does not maintain data for it.
                </p>
            </div>
        """)

    if "-" in str(symData["netChange"]):
        cardClr = "bg-danger"
        arrow = "↓" 
    elif symData["netPercentChangeInDouble"] == "0.00%":
        cardClr = "bg-secondary"
        arrow = "↔"
    else:
        cardClr = "bg-success"
        arrow = "↑"
    if len(symData["description"]) > 57:
        name = str(symData["description"])
        nameDisplay = f"{name[:54]}..."
    else:
        nameDisplay = symData["description"]
    quote = f"""
        <div class="card {cardClr} text-white">
            <div class="card-body">
                <h4>{sym}: {nameDisplay}</h4>
                <h6>
                    {arrow} {symData["netChange"]}
                    ({symData["netPercentChangeInDouble"]})
                </h6>
            </div>
        </div>
    """
    rows = ""
    for attr in symData:
        rows += f"""
            <tr>
                <th>{cfg.engAttrs[attr]}</th>
                <td>{symData[attr]}</td>
            </tr>
        """
    info = f"""
        <table id="table" class="table table-hover">
            <thead class="thead-light text-center">
                <tr>
                    <th colspan="2">{sym} Profile</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    """
    html = f"""
        <div class="modal-header">
            <h5 class="modal-title text-center">
                {sym} Stock Quote &amp; Information
            </h5>
            <button type="button" class="close" data-dismiss="modal">
                &times;
            </button>
        </div>
        <div class="modal-body" style="height: 80vh; overflow-y: auto;">
            {quote}
            <br>
            <div class="card bg-light text-center">
                <div id="chartCard" class="card-body"></div>
                <div class="card-footer">
                    <b>Graph Options</b>
                    <br>
                    <div class="row justify-content-center" style="padding-bottom: 10px">
                    <i>With Extended Hours:</i>&nbsp;&nbsp;
                    <button id="1dtrue" type="button" class="btn btn-sm btn-dark">
                        1d
                    </button>&nbsp;
                    <button id="3dtrue" type="button" class="btn btn-sm btn-dark">
                        3d
                    </button>&nbsp;
                    <button id="5dtrue" type="button" class="btn btn-sm btn-dark">
                        5d
                    </button>&nbsp;
                    <button id="10dtrue" type="button" class="btn btn-sm btn-dark">
                        10d
                    </button>&nbsp;
                    <button id="1mtrue" type="button" class="btn btn-sm btn-dark">
                        1m
                    </button>&nbsp;
                    <button id="3mtrue" type="button" class="btn btn-sm btn-dark">
                        3m
                    </button>&nbsp;
                    <button id="6mtrue" type="button" class="btn btn-sm btn-dark">
                        6m
                    </button>&nbsp;
                    <button id="1ytrue" type="button" class="btn btn-sm btn-dark">
                        1y
                    </button>&nbsp;
                    <button id="3ytrue" type="button" class="btn btn-sm btn-dark">
                        3y
                    </button>&nbsp;
                    <button id="5ytrue" type="button" class="btn btn-sm btn-dark">
                        5y
                    </button>&nbsp;
                    <button id="YTDtrue" type="button" class="btn btn-sm btn-dark">
                        YTD
                    </button>
                </div>
                <div class="row justify-content-center">
                    <i>Without Extended Hours:</i>&nbsp;&nbsp;
                    <button id="1dfalse" type="button" class="btn btn-sm btn-dark">
                        1d
                    </button>&nbsp;
                    <button id="3dfalse" type="button" class="btn btn-sm btn-dark">
                        3d
                    </button>&nbsp;
                    <button id="5dfalse" type="button" class="btn btn-sm btn-dark">
                        5d
                    </button>&nbsp;
                    <button id="10dfalse" type="button" class="btn btn-sm btn-dark">
                        10d
                    </button>&nbsp;
                    <button id="1mfalse" type="button" class="btn btn-sm btn-dark">
                        1m
                    </button>&nbsp;
                    <button id="3mfalse" type="button" class="btn btn-sm btn-dark">
                        3m
                    </button>&nbsp;
                    <button id="6mfalse" type="button" class="btn btn-sm btn-dark">
                        6m
                    </button>&nbsp;
                    <button id="1yfalse" type="button" class="btn btn-sm btn-dark">
                        1y
                    </button>&nbsp;
                    <button id="3yfalse" type="button" class="btn btn-sm btn-dark">
                        3y
                    </button>&nbsp;
                    <button id="5yfalse" type="button" class="btn btn-sm btn-dark">
                        5y
                    </button>&nbsp;
                    <button id="YTDfalse" type="button" class="btn btn-sm btn-dark">
                        YTD
                    </button>&nbsp;
                </div>
                </div>
            </div>
            <br>
            <div class="card bg-light">
                {info}
            </div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-dark" data-dismiss="modal">
                Close
            </button>
        </div>
        <script>
            $(function() {{
                $('#chartCard').load('/graph/{sym}/10d/True')
            }})
            document.getElementById("1dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/True');
            }}
            document.getElementById("3dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/True')
            }}

            document.getElementById("5dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/True')
            }}

            document.getElementById("10dtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/True')
            }}

            document.getElementById("1mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/True')
            }}

            document.getElementById("3mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/True')
            }}

            document.getElementById("6mtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/True')
            }}

            document.getElementById("1ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/True')
            }}

            document.getElementById("3ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/True')
            }}

            document.getElementById("5ytrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/True')
            }}

            document.getElementById("YTDtrue").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/True')
            }}

            document.getElementById("1dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/False');
            }}

            document.getElementById("3dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/False')
            }}

            document.getElementById("5dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/False')
            }}

            document.getElementById("10dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/False')
            }}

            document.getElementById("1mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/False')
            }}

            document.getElementById("3mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/False')
            }}

            document.getElementById("6mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/False')
            }}

            document.getElementById("1yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/False')
            }}

            document.getElementById("3yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/False')
            }}

            document.getElementById("5yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/False')
            }}

            document.getElementById("YTDfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/False')
            }}
        </script>
    """
    return flask.Markup(html)
