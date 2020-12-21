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

def getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo,
                   expMonth, standard):
    url = r"https://api.tdameritrade.com/v1/marketdata/chains"
    params = {"apikey": cfg.apikey,
              "symbol": sym,
              "contractType": conType,
              "strikeCount": numStrikes,
              "strategy": "SINGLE",
              "strike": strike,
              "range": rng,
              "fromDate": expFrom,
              "toDate": expTo,
              "expMonth": expMonth,
              "optionType": standard}
    content = rq.get(url, params).json()
    info = {"underlyingPrice": content["underlyingPrice"]}
    if conType == "ALL" or conType == "CALL":
        cols = ["Expiration", "Strike", "Bid", "Ask", "Market", "%Chg",
                "Volume", "Type", "ITM", "Name"]
        dfCalls = pd.DataFrame(columns = cols)
        for edKey in content["callExpDateMap"]:
            edGroup = content["callExpDateMap"][edKey]
            for strike in edGroup:
                option = edGroup[strike][0]
                newRow = [edKey, float(strike), option["bid"], option["ask"],
                          option["mark"], option["percentChange"],
                          option["totalVolume"], "call", option["inTheMoney"],
                          option["description"]]
                dfCalls.loc[len(dfCalls)] = newRow
        info["dfCalls"] = dfCalls
    if conType == "ALL" or conType == "PUT":
        cols = ["Expiration", "Strike", "Bid", "Ask", "Market", "%Chg",
                "Volume", "Type", "ITM", "Name"]
        dfPuts = pd.DataFrame(columns = cols)
        for edKey in content["putExpDateMap"]:
            edGroup = content["putExpDateMap"][edKey]
            for strike in edGroup:
                option = edGroup[strike][0]
                newRow = [edKey, float(strike), option["bid"], option["ask"],
                          option["mark"], option["percentChange"],
                          option["totalVolume"], "put", option["inTheMoney"],
                          option["description"]]
                dfPuts.loc[len(dfPuts)] = newRow
        info["dfPuts"] = dfPuts
    return info

