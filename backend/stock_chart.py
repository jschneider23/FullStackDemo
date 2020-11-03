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
def newGraph(sym, timeOption = "10d", hasExtHrs = True):
    # Will provide more robust settings options but currently implementing
    # basic functionality here
    chartCfg = cfg.chartMap.get(timeOption)
    texts = []

    url = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(sym)
    params = {"apikey": cfg.apikey,
              "periodType": chartCfg[1],
              "period": chartCfg[2],
              "frequencyType": chartCfg[3],
              "frequency": chartCfg[4],
              "needExtendedHoursData": str(hasExtHrs).lower()}
    candleList = rq.get(url, params).json().get("candles")

    dataPoints = []
    for candle in candleList:
        x = candle["datetime"]
        y = [candle["open"], candle["high"], candle["low"], candle["close"]]
        dataPoints.append({"x": x, "y:": y})

    if "$" in sym:
        texts.extend([sym + " Point History", "", "Points"])
    else:
        texts.extend([sym + " Price History", "$", "Price"])

    info = {"animationEnabled": True,
            "theme": "light2",
            "exportEnabled": False,
            "title": {
                "text": texts[0]
            },
            "subtitles": [{
                "text": "Over the Last " + chartCfg[0]
            }],
            "axisX": {
                "valueFormatString": chartCfg[5],
                "title": "Date"
            },
            "axisY": {
                "prefix": texts[1],
                "title": texts[2]
            },
            "data": [{
                "type": "candlestick",
                "xValueType": "dateTime",
                "dataPoints": dataPoints
            }]}
    return info

print(newGraph("TSLA"))
