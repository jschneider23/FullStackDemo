# File will have code that handles nearly all of the html formatting and
# processing from backend API data to keep app.py as clutter-free as possible

import json
import flask
from backend import stock_info as sinfo

def htmlIndexCard(indexSym):
    data = sinfo.getBySymbol(indexSym, "indexCard")
    lastPrice = round(data["lastPrice"], 2)
    closePrice = round(data["closePrice"], 2)
    netChange = round(data["netChange"], 2)
    netPercentChangeInDouble = round(data["netPercentChangeInDouble"], 2)
    if netChange < 0:
        html = (
        '<div class="row text-danger">'
        '<div class="col"><b><u>Last:</u></b><br>'
        '<span id="' + indexSym + 'lp">{}</span></div>'
        '<div class="col"><b><u>Close:</u></b><br>'
        '<span id="' + indexSym + 'cp">{}</span></div>'
        '<div class="col"><b><u>Value Chg:</u></b><br>'
        '<span id="' + indexSym + 'vchg">{}</span></div>'
        '<div class="col"><b><u>% Chg:</u></b><br>'
        '<span id="' + indexSym + 'pchg">{}%</div>'
        '</div>'
        ).format(lastPrice, closePrice, netChange, netPercentChangeInDouble)
    else:
        html = (
        '<div class="row text-success">'
        '<div class="col"><b><u>Last:</u></b><br>'
        '<span id="' + indexSym + 'lp">{}</span></div>'
        '<div class="col"><b><u>Close:</u></b><br>'
        '<span id="' + indexSym + 'cp">{}</span></div>'
        '<div class="col"><b><u>Value Chg:</u></b><br>'
        '<span id="' + indexSym + 'vchg">{}</span></div>'
        '<div class="col"><b><u>% Chg:</u></b><br>'
        '<span id="' + indexSym + 'pchg">{}%</div>'
        '</div>'
        ).format(lastPrice, closePrice, netChange, netPercentChangeInDouble)
    return flask.Markup(html)
#print(htmlIndexCard("$DJI"))
