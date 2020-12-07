# File will have code that handles nearly all of the html formatting and
# processing from backend API data to keep app.py as clutter-free as possible

import json
import flask
import pandas as pd
from backend import bd_config as cfg, stock_info as si, stock_chart as sc

def htmlIndexCard(indexSym):
    data = si.getBySymbol(indexSym, "indexCard")
    cardClr = "bg-danger" if float(data["netChange"]) < 0.0 else "bg-success"
    html = f"""
        <div class="row">
        <div class="col"><b><u>Last:</u></b><br>
        <span id=" + indexSym + lp">{data["lastPrice"]}</span></div>
        <div class="col"><b><u>Close:</u></b><br>
        <span id=" + indexSym + cp">{data["closePrice"]}</span></div>
        <div class="col"><b><u>Value Chg:</u></b><br>
        <span id=" + indexSym + vchg">{data["netChange"]}</span></div>
        <div class="col"><b><u>% Chg:</u></b><br>
        <span id=" + indexSym + pchg">{data["netPercentChangeInDouble"]}</div>
        </div>
    """
    return (cardClr, flask.Markup(html))

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
            <tr>
                <th>{cfg.engAttrs[attr]}</th>
                <td>{symData[attr]}</td>
            </tr>
        """
    info = f"""
        <table class="table table-hover">
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


