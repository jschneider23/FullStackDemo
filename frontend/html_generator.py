# File will have code that handles nearly all of the html formatting and
# processing from backend API data to keep app.py as clutter-free as possible

import json
import flask
import pandas as pd
from backend import bd_config as cfg, stock_info as si, stock_chart as sc

def htmlIndexCard(indexSym):
    data = si.getBySymbol(indexSym, "indexCard")
    lastPrice = round(data["lastPrice"], 2)
    closePrice = round(data["closePrice"], 2)
    netChange = round(data["netChange"], 2)
    netPercentChangeInDouble = round(data["netPercentChangeInDouble"], 2)
    cardColor = "bg-danger" if netChange < 0.0 else "bg-success"
    html = f"""
        <div class="row">
        <div class="col"><b><u>Last:</u></b><br>
        <span id=" + indexSym + lp">{lastPrice}</span></div>
        <div class="col"><b><u>Close:</u></b><br>
        <span id=" + indexSym + cp">{closePrice}</span></div>
        <div class="col"><b><u>Value Chg:</u></b><br>
        <span id=" + indexSym + vchg">{netChange}</span></div>
        <div class="col"><b><u>% Chg:</u></b><br>
        <span id=" + indexSym + pchg">{netPercentChangeInDouble}%</div>
        </div>
    """
    return (cardColor, flask.Markup(html))

def htmlModalData(sym):
    if "$" in sym:
        symData = si.getBySymbol(sym, "indexFull")
        title = f"{sym} Index Quote &amp; Information"
    else:
        symData = si.getBySymbol(sym)
        title = f"{sym} Stock Quote &amp; Information"
    if symData is None:
        return None
    quote = "Quote would go here"
    chart = f"""
        <script>
            window.onload = function () {{
            var chart = new CanvasJS.Chart("chart", {json.dumps(sc.newGraph(sym))});
            chart.render();
            }}
        </script>
    """
    rows = ""
    for attr in symData:
        rows += f"""
            <tr class="table-light">
                    <th>{cfg.engAttrs[attr]}</th>
                    <td>{symData[attr]}</td>
            </tr>
        """
    info = f"""
        <table class="table table-responsive">
            <thead class="thead-light">
                <tr>
                    <th colspan="2">{sym} Profile</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    """
    script = """
        <script>
            $('#viewStock').modal('show');
            console.log($('#viewStock'))
        </script>
    """
    return {"script": flask.Markup(script),
            "title": flask.Markup(title),
            "quote": flask.Markup(quote),
            "chart": flask.Markup(chart),
            "info": flask.Markup(info)}

def htmlNameResults(name):
    dfResults = si.getByName(name)
    if dfResults is None:
        html = f"""
            <h5>\"<i>{name}</i>\" doesn't exist as a valid name or name
            fragment matching any symbol(s) in TD's Database.  Please search
            for a valid name or name fragment or enter a valid symbol.</h5>
        """
    elif not isinstance(dfResults, pd.DataFrame):
        html = "TODO: Make this simulate a direct symbol lookup"
    else:
        rows = ""
        for ind in dfResults.index:
            rows += f"""
                <tr class="table-light">
                    <td>{dfResults["Symbol"][ind]}</td>
                    <td>{dfResults["Company Name"][ind]}</td>
                    <td>{dfResults["Type"][ind]}</td>
                    <td>{dfResults["Exchange"][ind]}</td>
                </tr>
            """
            print(rows)

        html = f"""
            <h3>Search Results For \"<i>{name}</i>\" Returned
            <i>{len(dfResults)} Results</i></h3>
            <br>
            <table class="table table-responsive">
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
        """
    return flask.Markup(html)

