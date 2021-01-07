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
    if "$" not in sym:
        rows += f"""
            <tr>
                <th>Options</th>
                <td>
                    <a id="{sym}OptionsLink" href="placeholder_href">
                        View Options (w/ Default Settings)
                    </a>
                </td>
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
                    <td>
                        <a id="{dfResults["Symbol"][ind]}ModalLink" href="testfornameresults">
                            {dfResults["Symbol"][ind]}
                        </a>
                    </td>
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
                $('#modalContent').load('/moverModalContent/{sym}')
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

def htmlMoverModal(sym):
    symData = si.getBySymbol(sym)
    if symData is None:
        return "Debug message delete this later: this is likely an api issue"

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
    if "$" not in sym:
        rows += f"""
            <tr>
                <th>Options</th>
                <td>
                    <a id="{sym}OptionsLink" href="placeholder_href">
                        View Options (w/ Default Settings)
                    </a>
                </td>
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
