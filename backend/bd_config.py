# Defines the apikey used to interact with registered TD Ameritrade App
apikey = "RMSSTUCHMW9W04BBKRM7EMIP9OGFVYAE"

# Defines the attributes retrieved in stock_info.py functions
infoAttrs = ["symbol", "description", "mark", "exchangeName", "assetType",
             "totalVolume", "divAmount", "divYield", "divDate", "netChange",
             "netPercentChangeInDouble"]

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
