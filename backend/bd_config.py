# Defines the api key used to interact with registered TD Ameritrade App
apikey = "PGPYQUOPSCQIBQDDSFAGSLOBBXD7BKJL"

# Defines the base url from which to do perform symbol lookup web-scraping
gbnUrl = "https://research.tdameritrade.com/grid/public/symbollookup/symbollookup.asp"
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
# values for the API call, as well as information required for html to render
# the candlestick charts in modals using Plotly.
chartMap = {
    "1d": {"engTime": "Trading Day", "periodType": "day", "period": 1,
           "freqType": "minute", "freq": 1, "fmt": "%-I:%M"},
    "3d": {"engTime": "3 Trading Days", "periodType": "day", "period": 3,
           "freqType": "minute", "freq": 15, "fmt": "%-I:%M"},
    "5d": {"engTime": "5 Trading Days", "periodType": "day", "period": 5,
           "freqType": "minute", "freq": 30, "fmt": "%-I:%M"},
    "10d": {"engTime": "10 Trading Days", "periodType": "day", "period": 10,
            "freqType": "minute", "freq": 30, "fmt": "%-I:%M"},
    "1m": {"engTime": "1 Trading Month", "periodType": "month", "period": 1,
           "freqType": "daily", "freq": 1, "fmt": "%b-%-d"},
    "3m": {"engTime": "3 Trading Months", "periodType": "month", "period": 3,
           "freqType": "daily", "freq": 1, "fmt": "%b-%-d"},
    "6m": {"engTime": "6 Trading Months", "periodType": "month", "period": 6,
           "freqType": "daily", "freq": 1, "fmt": "%b-%-d"},
    "1y": {"engTime": "1 Trading Year", "periodType": "year", "period": 1,
           "freqType": "daily", "freq": 1, "fmt": "%b-%y"},
    "3y": {"engTime": "3 Trading Years", "periodType": "year", "period": 3,
           "freqType": "weekly", "freq": 1, "fmt": "%b-%y"},
    "5y": {"engTime": "5 Trading Years", "periodType": "year", "period": 5,
           "freqType": "weekly", "freq": 1, "fmt": "%b-%y"},
    "YTD": {"engTime": "Trading Year to Date", "periodType": "year",
            "period": 1, "freqType": "daily", "freq": 1, "fmt": "%b-%-d"}
}