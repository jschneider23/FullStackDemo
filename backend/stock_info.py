# This file contains the functions that retrieve the necessary information
# from the appropriate TD Ameritrade Developer APIs and format the data to be
# used in other areas of the app based on a given symbol or stock name.

import requests as rq
import pandas as pd
from backend import bd_config as cfg, stock_aux as aux
from bs4 import BeautifulSoup as bs
import datetime as dt\

# For added details on the purpose and functionality of this module, see the
# README

# Requests the TD Ameritrade Quotes API for the stock's attributes that will
# eventually be displayed to the user on the frontend and returns a dictionary
# with each attribute and its corresponding value.  These attributes are
# defined in the config file and the README, and depend on whether the symbol
# is for a stock, index, or for the case when this is used for Index Cards for
# the "At a Glance..." Home Page Section.
def getBySymbol(sym, symType = ""):
    sym = sym.upper()
    url = f"https://api.tdameritrade.com/v1/marketdata/{sym}/quotes"
    params = {"apikey": cfg.apikey}
    content = rq.get(url, params).json()
    data = {}

    if len(content) == 0:
        return None

    if symType == "indexCard":
        for attr in cfg.cardAttrs:
            data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
        if sym == "$DJI":
            data["cardTitle"] = "Dow Jones Industrial Average"
        elif sym == "$SPX.X":
            data["cardTitle"] = "S&P 500"
        else:
            data["cardTitle"] = "NASDAQ Composite"
    elif symType == "indexFull":
        for attr in cfg.indexAttrs:
            data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
    else:
        for attr in cfg.infoAttrs:
            data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
    return data

# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to TD Ameritrade's symbol lookup page with
# appropriate url parameters to generate a table of all stock names containing
# name.  If there is only one table entry then this function returns the
# result of getBySymbol() with the associated symbol.  Otherwise, it will
# return a dictionary of all search results with symbol keys and stock name
# values.
def getByName(name):
    url = f"{cfg.gbnUrl}?text={name}"
    req = rq.get(url)
    root = bs(req.content, "lxml")
    html = root.find_all(class_ = "dataBackground")

    if len(html) == 0:
        return None
   
    df = pd.read_html(str(html[0]))[0]
    if len(df) == 1:
        return getBySymbol(df.iloc[0]["Symbol"])
    else:
        return df