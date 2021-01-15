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

manualApply = {
    "OTM": True,
    "ITM": True,
    "NTM": True,
    "SAK": False,
    "SBK": False,
    "SNK": False,
    "ALL": True
}

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
    if strike == "" or strike == "null":
        del params["strike"]
    if expFrom == "" or expFrom == "null":
        del params["fromDate"]
    if expTo == "" or expTo == "null":
        del params["toDate"]
    if numStrikes != "" and manualApply.get(rng):
        del params["strikeCount"]
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
        print("TD Filtered:\n" + str(info))
    trueInfo = trulyApplyFilters(info, numStrikes, strike, rng)
    return trueInfo

# Filter interactions that will remain disallowed for good reason:
# expFrom and expTo OR expMonth BUT NOT BOTH
# 
# Ones that need to be handled:
# Strike Price (cannot have _ selected)
# Range (cannot have _ selected)
#
# Also once filters are applied, need to add dummy rows so the expiration
# dates line up and one table doesn't end before the other
def trulyApplyFilters(info, numStrikes, strike, rng):
    if manualApply.get(rng) and numStrikes != "":
        dfCalls = info.get("dfCalls")
        dfPuts = info.get("dfPuts")
        if dfCalls is not None:
            newExp = None
            oldExp = None
            strikesLeftForExp = numStrikes
            for ind in dfCalls.index:
                newExp = dfCalls["Expiration"][ind]
                if oldExp is None:
                    strikesLeftForExp = int(numStrikes) - 1
                    oldExp = newExp
                elif strikesLeftForExp > 0:
                    strikesLeftForExp -= 1
                else:
                    dfCalls.drop(ind, inplace = True)
                    oldExp = None
            info["dfCalls"] = dfCalls.reset_index(drop = True)
        if dfPuts is not None:
            newExp = None
            oldExp = None
            strikesLeftForExp = numStrikes
            for ind in dfPuts.index:
                newExp = dfPuts["Expiration"][ind]
                if oldExp is None:
                    strikesLeftForExp = int(numStrikes) - 1
                    oldExp = newExp
                elif strikesLeftForExp > 0:
                    strikesLeftForExp -= 1
                else:
                    dfPuts.drop(ind, inplace = True)
                    oldExp = None
            info["dfPuts"] = dfPuts.reset_index(drop = True)
    print("FULLLY FILTERED (gOC ret):\n" + str(info))
    return info

sym = "TSLA"
conType = "ALL"
numStrikes = "4"
strike = ""
rng = "OTM"
expFrom = ""
expTo = ""
expMonth = ""
standard = "ALL"
# Return for just TSLA with all other at default or blank is both calls and
# puts table 3863 entries long
# rng: can't have numStrikes if its "_-the-money" based, but needs it if
# it is strike-based
# strike: this is the priortized filter over most others, can't have numStrikes
# strike can be used with money status but will result in an empty df for
# either calls or puts, nullifies any strike-based range
# numStrikes will nullify the strike price filter
# combining all 3 has numStrikes with priority
# Ensure all possible combinations work as intended:
# numStrikes and strike-> have 10 strikes default but disable if strike entered
# numStrikes and rng->apply rng first, then apply numStrikes if rng is $-based
# strike and rng->account for empty df if is $-based rng, add strike-based func
# All 3 at the same time->disable numStrikes if strike entered
#getOptionChain(sym, conType, numStrikes, strike, rng, expFrom, expTo, expMonth, standard)
