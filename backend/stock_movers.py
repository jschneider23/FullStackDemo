# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the top movers
# information for various indicies into organized dataframes that can easily
# be accessed and manipulated when displaying to the front-end.

import requests as rq
import pandas as pd
from backend import bd_config as cfg

# For added details on the purpose and functionality of this module, see the
# README

# Requests the TD Ameritrade Movers API to retrieve mover information based on
# the given parameters as a dataframe.  Movers can be retrieved for any TD
# Ameritrade supported index in either "gainer" or "loser" direction and the
# change can be in units of value or by percentage.  Last price also retrieved.
def getMovers(index, direction, change):
    url = r"https://api.tdameritrade.com/v1/marketdata/{}/movers".format(index)
    params = {"apikey": cfg.apikey,
              "direction": direction,
              "change": change}
    movers = rq.get(url, params).json()
    if type(movers) == dict:
        return None

    df = pd.DataFrame(columns = ["symbol", "name", "change", "last"])
    for m in movers:
        chg = m["change"]
        if change == "percent":
            chg = f"{format(round(chg * 100, 2), '.2f')}%"
        else:
            chg = f"${format(round(chg, 2), '.2f')}"
        if "-" in str(chg):
            chg = f"↓&nbsp;{chg}"
        elif str(chg) == "0.00" or str(chg) == "0.00%":
            chg = f"↔&nbsp;{chg}"
        else:
            chg = f"↑&nbsp;{chg}"
        last = f"${format(round(m['last'], 2), '.2f')}"
        newRow = [m["symbol"], m["description"], chg, last]
        df.loc[len(df)] = newRow
    return df

