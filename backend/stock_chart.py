# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the data to be
# used to create stock and index price/value history graphs based on a given
# set of parameters that are provided by the user on the front end.  It also
# provides a function that allows editing of the display style of an existing
# set of graph data (such as line color) without unnecessary API calls.

import requests as rq
import config as cfg
import pandas as pd
import seaborn as sb

def newGraph(sym, perType = "day", per = 10, freqType = "minute",
                   freq = 1, hasExtHrs = True):
    graph = None
    return graph

def styleGraph(graph, useCandles, lineClr, ptType, ptClr, useShade, shadeClr,
               showMinMax):
    return graph
