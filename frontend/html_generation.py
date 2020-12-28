# File will have code that handles nearly all of the html formatting and
# processing from backend API data to keep app.py as clutter-free as possible

import json
import flask
import pandas as pd
from backend import bd_config as cfg, stock_info as si, stock_chart as sc, stock_movers as sm, stock_options as so
from frontend import fr_objects as frobj

# *** Home Page Generator Functions *** #
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
    html = f"""
        <div class="row">
        <div class="col"><b><u>Last:</u></b><br>
        <span id=" + indexSym + lp">{data["lastPrice"]}</span></div>
        <div class="col"><b><u>Close:</u></b><br>
        <span id=" + indexSym + cp">{data["closePrice"]}</span></div>
        <div class="col"><b><u>Value Chg:</u></b><br>
        <span id=" + indexSym + vchg">{arrow} {data["netChange"]}</span></div>
        <div class="col"><b><u>% Chg:</u></b><br>
        <span id=" + indexSym + pchg">
        {arrow} {data["netPercentChangeInDouble"]}</div>
        </div>
    """
    return {"color": cardClr, "html": flask.Markup(html)}

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
    graphOptions = f"""
        <b>Graph Options</b>
        <br>
        With Extended Hours:
        <button id="btn1d" type="button" class="btn btn-sm btn-dark">
            1d
        </button>
        <button id="btn3d" type="button" class="btn btn-sm btn-dark">
            3d
        </button>
        <button id="btn5d" type="button" class="btn btn-sm btn-dark">
            5d
        </button>
        <button id="btn10d" type="button" class="btn btn-sm btn-dark">
            10d
        </button>
        <button id="btn1m" type="button" class="btn btn-sm btn-dark">
            1m
        </button>
        <button id="btn3m" type="button" class="btn btn-sm btn-dark">
            3m
        </button>
        <button id="btn6md" type="button" class="btn btn-sm btn-dark">
            6m
        </button>
        <button id="btn1y" type="button" class="btn btn-sm btn-dark">
            1y
        </button>
        <button id="btn3y" type="button" class="btn btn-sm btn-dark">
            3y
        </button>
        <button id="btn5y" type="button" class="btn btn-sm btn-dark">
            5y
        </button>
        <button id="btnYTD" type="button" class="btn btn-sm btn-dark">
            YTD
        </button>
        <hr>
        Without Extended Hours:
        <button id="btn1dfalse" type="button" class="btn btn-sm btn-dark">
            1d
        </button>
        <button id="btn3dfalse" type="button" class="btn btn-sm btn-dark">
            3d
        </button>
        <button id="btn5dfalse" type="button" class="btn btn-sm btn-dark">
            5d
        </button>
        <button id="btn10dfalse" type="button" class="btn btn-sm btn-dark">
            10d
        </button>
        <button id="btn1mfalse" type="button" class="btn btn-sm btn-dark">
            1m
        </button>
        <button id="btn3mfalse" type="button" class="btn btn-sm btn-dark">
            3m
        </button>
        <button id="btn6mdfalse" type="button" class="btn btn-sm btn-dark">
            6m
        </button>
        <button id="btn1yfalse" type="button" class="btn btn-sm btn-dark">
            1y
        </button>
        <button id="btn3yfalse" type="button" class="btn btn-sm btn-dark">
            3y
        </button>
        <button id="btn5yfalse" type="button" class="btn btn-sm btn-dark">
            5y
        </button>
        <button id="btnYTDfalse" type="button" class="btn btn-sm btn-dark">
            YTD
        </button>
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
            $('#chartCard').load('/graph/{sym}/10d/True', function() {{
            document.getElementById("btn1d").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/True');
            }}

            document.getElementById("btn3d").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/True')
            }}

            document.getElementById("btn5d").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/True')
            }}

            document.getElementById("btn10d").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/True')
            }}

            document.getElementById("btn1m").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/True')
            }}

            document.getElementById("btn3m").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/True')
            }}

            document.getElementById("btn6m").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/True')
            }}

            document.getElementById("btn1y").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/True')
            }}

            document.getElementById("btn3y").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/True')
            }}

            document.getElementById("btn5y").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/True')
            }}

            document.getElementById("btnYTD").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/True')
            }}


            document.getElementById("btn1dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1d/False');
            }}

            document.getElementById("btn3dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3d/False')
            }}

            document.getElementById("btn5dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5d/False')
            }}

            document.getElementById("btn10dfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/10d/False')
            }}

            document.getElementById("btn1mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1m/False')
            }}

            document.getElementById("btn3mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3m/False')
            }}

            document.getElementById("btn6mfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/6m/False')
            }}

            document.getElementById("btn1yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/1y/False')
            }}

            document.getElementById("btn3yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/3y/False')
            }}

            document.getElementById("btn5yfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/5y/False')
            }}

            document.getElementById("btnYTDfalse").onclick = function() {{
                $('#chartCard').load('/graph/{sym}/YTD/False')
            }}
        }})}})
    """
    return {"script": flask.Markup(script),
            "title": flask.Markup(title),
            "quote": flask.Markup(quote),
            "graphOptions": flask.Markup(graphOptions),
            "info": flask.Markup(info)}

def htmlNameResults(name):
    dfResults = si.getByName(name)
    if dfResults is None:
        return None
    elif not isinstance(dfResults, pd.DataFrame):
        html = "TODO: Make this simulate a direct symbol lookup"
    else:
        rows = ""
        for ind in dfResults.index:
            rows += f"""
                <tr>
                    <td>{dfResults["Symbol"][ind]}</td>
                    <td>{dfResults["Company Name"][ind]}</td>
                    <td>{dfResults["Type"][ind]}</td>
                    <td>{dfResults["Exchange"][ind]}</td>
                </tr>
            """

        html = f"""
            <div class="card bg-light">
                <h3 class="text-center card-header">
                    Name Search For \"<i>{name}</i>\" Returned <i>
                    {len(dfResults)} Results</i>
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
            </div>
        """
    return flask.Markup(html)

# *** Options Page Functions ***#

def htmlOCModalData(sym, conType, numStrikes, strike, rng, expFrom, expTo,
                    expMonth, standard):
    debug = f"""
        Params sending to backend:
        sym: {sym}
        conType: {conType}
        numStrikes: {numStrikes}
        strike: {strike}
        rng: {rng}
        expFrom: {expFrom}
        expTo: {expTo}
        expMonth: {expMonth}
        standard: {standard}
    """
    print(debug)
    errorMsg = ""
    try:
        ocDict = so.getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)
        underlyingPrice = ocDict.get("underlyingPrice")
        dfCalls = ocDict.get("dfCalls")
        dfPuts = ocDict.get("dfPuts")
    except:
        errorMsg = f"""
            There was an error finding an Option Chain for \"<i>{sym}</i>\" 
            with the given filters.  Either \"<i>{sym}</i>\" is a
            non-optionable symbol or invalid parameters were provided.
        """
        return {"errorMsg": errorMsg}

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
                    call = frobj.Option.fromRow(ind, underlyingPrice, row)
                    callList.append(call)
                    oldExpDate = newExpDate
                else:
                    edg = frobj.OptionEDG.fromOptionLists(callList = callList)
                    expDateGroups.append(edg)
                    callList = []
                    oldExpDate = None
        elif dfPuts is not None and dfCalls is None:
            if ind < len(dfPuts):
                row = dfPuts.loc[ind]
                newExpDate = row["Expiration"]
                if oldExpDate is None or oldExpDate == newExpDate:
                    put = frobj.Option.fromRow(ind, underlyingPrice, row)
                    callList.append(put)
                    oldExpDate = newExpDate
                else:
                    edg = frobj.OptionEDG.fromOptionLists(putList = putList)
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
                call = frobj.Option.fromRow(ind, underlyingPrice, callRow)
                put = frobj.Option.fromRow(ind, underlyingPrice, putRow)
                callList.append(call)
                putList.append(put)
                oldExpDate = newExpDate
            else:
                edg = frobj.OptionEDG.fromOptionLists(callList = callList, putList = putList)
                expDateGroups.append(edg)
                callList = []
                putList = []
                oldExpDate = None
    oc = frobj.OptionChain(sym, underlyingPrice, expDateGroups)
    htmlDict = oc.htmlOCAccordian()
    return {"script": flask.Markup(htmlDict["script"]),
            "title": flask.Markup(htmlDict["title"]),
            "oc": flask.Markup(htmlDict["oc"]),
            "errorMsg": flask.Markup(errorMsg)}

# *** Movers Page Functions *** #
def htmlMoverCard(indexSym, direction, change):
    dfMovers = sm.getMovers(indexSym, direction, change)
    rows = ""
    ind = None
    for ind in dfMovers.index:
        rows += f"""
            <tr class="text-white">
                <th>{int(ind)+1}</th>
                <td>{dfMovers["symbol"][ind]}</td>
                <td>{dfMovers["name"][ind]}</td>
                <td>{dfMovers["change"][ind]}</td>
                <td>{dfMovers["last"][ind]}</td>
            </tr>
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
    """
    return flask.Markup(html)
