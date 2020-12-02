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
    cardColor = "bg-danger" if netChange < 0.0 else "bg-success"
    html = """
        <div class="row">
        <div class="col"><b><u>Last:</u></b><br>
        <span id=" + indexSym + lp">{}</span></div>
        <div class="col"><b><u>Close:</u></b><br>
        <span id=" + indexSym + cp">{}</span></div>
        <div class="col"><b><u>Value Chg:</u></b><br>
        <span id=" + indexSym + vchg">{}</span></div>
        <div class="col"><b><u>% Chg:</u></b><br>
        <span id=" + indexSym + pchg">{}%</div>
        </div>
        """.format(lastPrice, closePrice, netChange, netPercentChangeInDouble)
    return (cardColor, flask.Markup(html))

def htmlModal(sym):
    html = """
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{} Title</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                {} Information
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
    """.format(sym, sym)
    return flask.Markup(html)
#print(htmlIndexCard("$DJI"))
