# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the option
# chain information for a given symbol from the API into a cleaned-up, easier
# to interpret, and simpler dataframe that can be understood by those without
# an advanced background in stock options, as well as making things quicker
# and more streamlined for the front-end to read and display.

import requests as rq
import pandas as pd
import json as js 
from backend import bd_config as cfg

def getOptionChain(sym, conType, numStrikes, hasQuotes, strike, rng, expFrom,
                   expTo, expMonth, optType):
    url = r"https://api.tdameritrade.com/v1/marketdata/chains"
    params = {"apikey": cfg.apikey,
              "symbol": sym,
              "contractType": conType,
              "strikeCount": numStrikes,
              "includeQuotes": hasQuotes,
              "strategy": "SINGLE",
              #"strike": strike,
              "range": rng,
              #"fromDate": expFrom,
              #"toDate": expTo,
              "expMonth": expMonth,
              "optionType": optType
              }
    if strike is not None:
        params["strike"] = strike
    if expFrom is not None:
        params["fromDate"] = expFrom
    if expTo is not None:
        params["toDate"] = expTo
    content = rq.get(url, params).json()
    info = [content["underlyingPrice"], None, None]
    if conType == "ALL" or conType == "CALL":
        cols = ["Expiration", "Strike", "Bid", "Ask", "Market", "%Chg", "Type",
                "ITM", "Name"]
        dfCalls = pd.DataFrame(columns = cols)
        for edKey in content["callExpDateMap"]:
            edGroup = content["callExpDateMap"][edKey]
            for strike in edGroup:
                option = edGroup[strike][0]
                newRow = [edKey, float(strike), option["bid"], option["ask"],
                          option["mark"], option["percentChange"], "Call",
                          option["inTheMoney"], option["description"]]
                dfCalls.loc[len(dfCalls)] = newRow
        info[1] = dfCalls
    if conType == "ALL" or conType == "PUT":
        cols = ["Expiration", "Strike", "Bid", "Ask", "Market", "%Chg", "Type",
                "ITM", "Name"]
        dfPuts = pd.DataFrame(columns = cols)
        for edKey in content["callExpDateMap"]:
            edGroup = content["callExpDateMap"][edKey]
            for strike in edGroup:
                option = edGroup[strike][0]
                newRow = [edKey, float(strike), option["bid"], option["ask"],
                          option["mark"], option["percentChange"], "Put",
                          option["inTheMoney"], option["description"]]
                dfPuts.loc[len(dfPuts)] = newRow
        info[2] = dfPuts
    return info


#getOptionChain("TSLA", "ALL", 10, "FALSE", None, "ALL", None, None, "NOV", "ALL")

