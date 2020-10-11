# This file contains the functions that retrieve the necessary information
# from the appropriate TD Ameritrade Developer APIs and format the data to be
# used in other areas of the app based on a given symbol or stock name.

import requests as rq
import config as cfg
from bs4 import BeautifulSoup as bsp

# ** Description:
# Requests the TD Ameritrade Quotes API for the stock's attributes that will
# eventually be displayed to the user on the frontend and returns a dictionary
# with each attribute and its corresponding value.  These attributes are
# the stock's: Symbol, Name, Current Market Value, Exchange, Asset Type,
# Volume, Dividend (Amt, yield, next date), and Value Change in both decimal and percent
#
# ** Prequesites:
# sym is a symbol 1 to 5 characters A-Z case-insensitive but not necessarily an
# exisiting market symbol (this is handled within this method)
#
# ** Returns:
# dict of {attribute: value}
def getBySymbol(sym):
    sym = sym.upper()
    url = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format(sym)
    params = {"apikey": cfg.apikey}
    content = rq.get(url, params).json()
    data = {}

    for attr in cfg.infoAttrs:
        data[attr] = content.get(sym).get(attr)

    return data

# ** Description:
# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to each exchange's website until a match is found.
# This function scrapes (in order, until found) the symbol-company name listing
# of the NYSE, NASDAQ, and AMEX.  After finding the symbol match, it then
# returns getBySymbol(symbol) in order to avoid redundant code.  This data
# is sourced from http://www.advfn.com.
#
# ** Prequesites:
# name is a case-insenstive string containing a potentially matchable stock
# name with or withouth whitespace (this will be trimmed)
#
# ** Returns:
# dict of {atrribute: value}
def getByName(name):
    symbol = ""
    return getBySymbol(symbol)

print(getBySymbol("TSLA"))