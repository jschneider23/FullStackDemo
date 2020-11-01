# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the data to be
# used on the front-end to create stock and index price/value history charts
# based on a given set of parameters that are provided by the user, using
# canvas.js.

import requests as rq
import config as cfg
import pandas as pd
import datetime as dt

# This code based off of using canvas.js in front end later, do documentation
# for this method after deciding.  Data will be formatted in a way to make
# it easier for front end.
def newGraph(sym, timeOption, hasExtHrs = True):
    # Will provide more robust settings options but currently implementing
    # basic functionality here
    chartCfg = cfg.chartMap.get(timeOption)
    texts = []
    if "$" in sym:
        texts[0] = sym + " Point History"
        texts[1] = ""
    else:
        texts[0] = sym + " Price History"
        texts[1] = "$"
    opts = {"animationEnabled": True,
            "theme": "light2",
            "exportEnabled": False,
            "title": {
                "text": texts[0]
            },
            "subtitles": [{
                "text": "Over the Last " + chartCfg[0]
            }]
            "axisX": {
                "valueFormatString": chartCfg[5],
                "title": "Date"
            }
            "axisY": {
                "prefix": texts[1],
                "title": "Value"
            }
            "toolTip": {
                content: "Date: {x}<br /><strong>Price:</strong><br />Open: "
                         + "{y[0]}, Close: {y[3]}<br />High: {y[1]}, Low: "
                         + "{y[2]}"
            }
            }
    data = None
    return (opts, data)
