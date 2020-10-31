# This file contains the function that retrieves the necessary information
# from the appropriate TD Ameritrade Developer APIs and formats the data to be
# used on the front-end to create stock and index price/value history charts
# based on a given set of parameters that are provided by the user, using
# canvas.js.

import requests as rq
import config as cfg
import pandas as pd

# This code based off of using canvas.js in front end later, do documentation
# for this method after deciding.  Data will be formatted in a way to make
# it easier for front end.
def newGraph(sym, perType = "day", per = 10, hasExtHrs = True):
    # Will provide more robust settings options but currently implementing
    # basic functionality here
    opts = {"animationEnabled": True,
            "theme": "light2",
            "exportEnabled": False,
            "title": {
                text: r"{} Price History".format(sym)
            },
            "subtitles": [{
                text: r"Over last {} {}(s)".format(per, perType)
            }]}
    data = None
    return (opts, data)

# This function will likely not be needed if canvas.js approach is used
def styleGraph(graph, useCandles, lineClr, ptType, ptClr, useShade, shadeClr,
               showMinMax):
    return graph

# Take care of opts that are dependent on the period as well as the freqType
# and freq to send to the payload
def periodDependentSettings(perType, per):
    # Switch that takes perType and decides what format x axis will follow
    mapFreq = {

    }
    freqType =
    freq = 
    xAxisFormat = {
        "day": "h:mm",
        "month": 
    }
