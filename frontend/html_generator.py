# File will have code that handles nearly all of the html formatting and
# processing from backend API data to keep app.py as clutter-free as possible

import json
import flask
from backend import stock_info as sinfo

def htmlIndexCard(indexSym):
    data = sinfo.getBySymbol(indexSym, "indexCard")
    html = "<h5>{}</h5><br>Change: {} ({}%)".format(data["lastPrice"],
           data["netChange"], round(data["netPercentChangeInDouble"], 2))
    return flask.Markup(html)
#print(htmlIndexCard("$DJI"))
