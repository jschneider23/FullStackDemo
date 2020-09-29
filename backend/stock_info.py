# This file contains the functions that retrieve the necessary information
# from the appropriate TD Ameritrade Developer APIs and format the data to be
# used in other areas of the app based on a given symbol or stock name.

import

# Requests the TD Ameritrade Quotes API for the stock's attributes that will
# eventually be displayed to the user on the frontend and returns a dictionary
# with each attribute and its corresponding value.  These attributes are
# the stock's: Symbol, Name, Current Market Value, Exchange, Asset Type,
# Volume, Outstanding Shares, and Dividend
def getBySymbol(symbol):
    return {}

# Searching by stock name requires a symbol lookup on an exchange's symbol
# list via a GET Request to each exchange's website until a match is found.
# This function scrapes (in order, until found) the symbol-company name listing
# of the NYSE, NASDAQ, and AMEX.  After finding the symbol match, it then
# returns getBySymbol(symbol) in order to avoid redundant code.
def getByName(name):
    symbol = ""
    return getBySymbol(symbol)