# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the data to
# create candlestick and line charts using Plotly.  These charts are then
# sent to the frontend to be used when viewing a stock or index proifle modal.

import requests as rq
import plotly.graph_objects as pgo
import plotly.io as pio
import pandas as pd
import json as js
import chart_studio.tools as cst
from backend import bd_config as cfg
from datetime import datetime as dt

def createGraph(sym, time = "10d", hasExtHrs = True):
    timeCfg = cfg.graphMap.get(time)
    url = f"https://api.tdameritrade.com/v1/marketdata/{sym}/pricehistory"
    params = {"apikey": cfg.apikey,
              "periodType": timeCfg["periodType"],
              "period": timeCfg["period"],
              "frequencyType": timeCfg["freqType"],
              "frequency": timeCfg["freq"],
              "needExtendedHoursData": str(hasExtHrs).lower()}
    
    candleList = rq.get(url, params).json().get("candles")
    dts = []
    opens = []
    highs = []
    lows = []
    closes = []
    for candle in candleList:
        dtConvert = dt.fromtimestamp(candle["datetime"] / 1000)
        dtFormat = dtConvert.strftime(timeCfg["fmt"])
        dts.append(dtFormat)
        opens.append(candle["open"])
        highs.append(candle["high"])
        lows.append(candle["low"])
        closes.append(candle["close"])

    if "$" in sym:
        title = f"{sym} Stock Price History (Over Last {timeCfg['engTime']})"
        yaxis = "Price (in $)"
    else:
        title = f"{sym} Index Point History (Over Last {timeCfg['engTime']})"
        yaxis = "Value (in Pts.)"
    if timeCfg["engTime"] != "1 Day":
        xaxis = "Date"
    else:
        xaxis = "Time"
    if hasExtHrs:
        xaxis += " (Includes Extended Hours Trading)"
    else:
        xaxis += " (Normal Trading Hours Only)"
    fig = pgo.Figure(data = [pgo.Candlestick(x = dts, open = opens,
                     high = highs, low = lows, close = closes)])
    fig.update_layout(title = title, yaxis_title = yaxis, xaxis_title = xaxis)

    filename = f"graph{sym}{time}{hasExtHrs}.html"
    pio.write_html(fig, file = f"frontend/graphs/{filename}")

def createAllGraphs(sym):
    for time in cfg.graphMap.keys():
        createGraph(sym, time, True)
        createGraph(sym, time, False)