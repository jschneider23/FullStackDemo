# This file contains the functions that retrieve the necessary information
# from the appropriate TD Ameritrade Developer APIs and format the data to be
# used in other areas of the app based on a given symbol or stock name.

import requests as rq
import pandas as pd
from backend import bd_config as cfg, stock_aux as aux
from bs4 import BeautifulSoup as bs
import datetime as dt
# ** Description **:
# Requests the TD Ameritrade Quotes API for the stock's attributes that will
# eventually be displayed to the user on the frontend and returns a dictionary
# with each attribute and its corresponding value.  These attributes are
# the stock's: Symbol, Name, Current Market Value, Exchange, Asset Type,
# Volume, Dividend (Amt, yield, next date), and Value Change in both decimal
# and percent
#
# ** Parameters **:
# sym is a symbol 1 to 5 characters A-Z case-insensitive but not necessarily an
# exisiting market symbol
#
# ** Returns **:
# dict of {attribute: value} of string attributes and various value types
def getBySymbol(sym, symType = ""):
    # TODO: Reduce/specify attributes for when sym is an index
    sym = sym.upper()
    url = f"https://api.tdameritrade.com/v1/marketdata/{sym}/quotes"
    params = {"apikey": cfg.apikey}
    content = rq.get(url, params).json()
    data = {}

    if len(content) == 0:
        return None
    else:
        if symType == "indexCard":
            for attr in cfg.cardAttrs:
                data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
        elif symType == "indexFull":
            for attr in cfg.indexAttrs:
                data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
        else:
            for attr in cfg.infoAttrs:
                data[attr] = aux.attrFormat(sym, attr, content[sym][attr])
        return data

# ** Description **:
# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to TD Ameritrade's symbol lookup page with
# appropriate url parameters to generate a table of all stock names containing
# name.  If there is only one table entry then this function returns the
# result of getBySymbol(symbol).  Otherwise, it will return a dictionary of
# all search results with symbol keys and stock name values.
#
# ** Parameters **:
# name is a case-insenstive string containing a potentially matchable stock
# name with or withouth whitespace (this will be trimmed)
#
# ** Returns **:
# dict of {atrribute: value} or dict of {symbol: stock name}
def getByName(name):
    url = f"{cfg.gbnUrl}?text={name}"
    req = rq.get(url)
    root = bs(req.content, "lxml")
    html = root.find_all(class_ = "dataBackground")

    if len(html) == 0:
        return None
    else:
        df = pd.read_html(str(html[0]))[0]
        
        if len(df) == 1:
            return getBySymbol(df.iloc[0]["Symbol"])
        else:
            return df

# def postgbn(name):
#     url = "https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp"
#     session = rq.Session()
#     reqGet = session.get(f"{url}?text={name}")
#     rootGet = bs(reqGet.content, "lxml")
#     formInputs = rootGet.select("input[name]")
#     payload = {item["name"]:item.get("value", "") for item in formInputs}
#     print(payload)
#     reqPost = session.get(url, data = payload)
#     rootPost = bs(reqPost.content, "lxml")
#     print(rootPost)
#     html = rootPost.find_all(class_ = "dataBackground")

#     if len(html) == 0:
#         return None
#     else:
#         df = pd.read_html(str(html[0]))[0]
        
#         if len(df) == 1:
#             return getBySymbol(df.iloc[0]["Symbol"])
#         else:
#             return df

# print(postgbn("coffee"))