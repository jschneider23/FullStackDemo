# This file contains the functions that retrieve the necessary information
# from the appropriate TD Ameritrade Developer APIs and format the data to be
# used in other areas of the app based on a given symbol or stock name.

import requests as rq
import config as cfg
import pandas as pd
from bs4 import BeautifulSoup as bs

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
def getBySymbol(sym):
    # TODO: Reduce/specify attributes for when sym is an index
    sym = sym.upper()
    url = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format(sym)
    params = {"apikey": cfg.apikey}
    content = rq.get(url, params).json()
    data = {}

    if len(content) == 0:
        return None
    else:
        for attr in cfg.infoAttrs:
            data[attr] = content.get(sym).get(attr)

        return data

# ** Description **:
# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to TD Ameritrade's symbol lookup page with
# appropriate url parameters to generate a table of all stock names containing
# name.  If there is only one table entrym then this function returns the
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
    url = r"https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp?text={}".format(name)
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
print(getByName("LKNCY"))