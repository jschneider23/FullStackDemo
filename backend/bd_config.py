# Defines the apikey used to interact with registered TD Ameritrade App
apikey = "RMSSTUCHMW9W04BBKRM7EMIP9OGFVYAE"

# Defines the attributes retrieved in getBySymbol() for an index card
cardAttrs = ["lastPrice", "closePrice", "netChange", 
             "netPercentChangeInDouble"]

# Defines the attributes retrieved in getBySymbol() for an index in full
indexAttrs = ["symbol", "description", "lastPrice", "netChange",
              "netPercentChangeInDouble", "openPrice", "lowPrice",
              "highPrice", "closePrice"]

# Defines the attributes retrieved in getBySymbol() if it is not an index
infoAttrs = ["symbol", "description", "mark", "netChange",
             "netPercentChangeInDouble", "exchangeName", "assetType",
             "totalVolume", "divAmount", "divYield", "divDate"]

# Defines the attributes that need to be rounded in attrFormat()
roundedAttrs = ["lastPrice", "closePrice", "netChange",
                "netPercentChangeInDouble", "openPrice", "lowPrice",
                "highPrice", "mark", "divAmount", "divYield"]

# Defines number attributes that need commas added between thousands
commaAttrs = ["lastPrice", "closePrice", "netChange",
              "netPercentChangeInDouble", "openPrice", "lowPrice",
              "highPrice", "mark", "totalVolume", "divAmount"]

# Defines the attributes that need a % sign after their value
percentAttrs = ["netPercentChangeInDouble", "divYield"]

# Defines the attributes that MAY need a $ sign before their value (depends
# on whether it is an index or stock)
moneyAttrs = ["mark", "netChange", "divAmount"]

# Dictionary that maps the TD API attribute names to readable english form
engAttrs = {
    "lastPrice": "Last",
    "closePrice": "Close",
    "netChange": "Day Change (Value)",
    "netPercentChangeInDouble": "Day Change (%)",
    "symbol": "Symbol",
    "description": "Name",
    "openPrice": "Open",
    "lowPrice": "Low",
    "highPrice": "High",
    "mark": "Market Price",
    "exchangeName": "Exchange",
    "assetType": "Stock Type",
    "totalVolume": "Volume",
    "divAmount": "Dividend $",
    "divYield": "Dividend Yield",
    "divDate": "Next Dividend Date"
}


# Defines the mapping of all chart time options (ex. "1y", "3m", "5d" meaning
# "1 year", "3 month", and "5 day" history respectively) to appropriate
# values for the API call as well as x axis unit format. Tuples are of format:
# (english meaning for subtitle, periodType, period, frequencyType, frequency, 
# canvas.js format string)
chartMap = {
    "1d": ("1 Day", "day", 1, "minute", 1, "h:mm"),
    "3d": ("3 Days", "day", 3, "minute", 15, "DDD M/DD"),
    "5d": ("5 Days", "day", 5, "minute", 30, "DDD M/DD"),
    "10d": ("10 Days", "day", 10, "minute", 30, "M/DD"),
    "1m": ("1 Month", "month", 1, "daily", 1, "M/DD"),
    "3m": ("3 Months", "month", 3, "daily", 1, "M/DD"),
    "6m": ("6 Months", "month", 6, "daily", 1, "M/DD"),
    "1y": ("1 Year", "year", 1, "daily", 1, "M/YY"),
    "3y": ("3 Years", "year", 3, "weekly", 1, "M/YY"),
    "5y": ("5 Years", "year", 5, "weekly", 1, "M/YY"),
    "YTD": ("Year to Date", "year", 1, "daily", 1, "M/DD")
}
