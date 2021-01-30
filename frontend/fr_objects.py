# This file contains class and function definitions that are used to implement
# the Options page on the frontend, both to handle server and backend data as
# well as format html to be displayed to the user.  Note that any html produced
# in this file still needs to be wrapped by flask as valid Markup, which is
# done in app.py (TENTATIVE, MIGHT CHANGE THIS LATER)

import pandas as pd
from datetime import datetime as dt

# Represents a single Option
class Option:
    # Standard Constructor for creating an Option object from each individual
    # property (not from the returned getOptionChain() dictionary)
    def __init__(self, dfIndex, underlyingPrice, expiration, strikePrice, bid,
                 ask, market, percentChange, volume, optionType, itm, name):
        self.optionID = f"{optionType}{dfIndex}"
        self.underlyingPrice = "{:,}".format(float(underlyingPrice))

        expiration = expiration[:expiration.index(":")]
        dtObjExp = dt.strptime(expiration, "%Y-%m-%d")
        self.expiration = dtObjExp.strftime("%b %d %Y")

        self.strikePrice = format(float(strikePrice), ".2f")
        self.bid = format(float(bid), ".2f")
        self.ask = format(float(ask), ".2f")
        self.market = format(float(market), ".2f")
        self.percentChange = format(float(percentChange), ".2f")
        self.volume = "{:,}".format(int(volume))
        self.optionType = optionType
        self.itm = itm
        self.name = name

    # Creates an Option object directly from a provided index, underlyingPrice,
    # and getOptionChain() dataframe retrieved by using iloc
    @classmethod
    def fromRow(cls, dfIndex, underlyingPrice, row):
        return cls(dfIndex, underlyingPrice, row["Expiration"], row["Strike"],
                   row["Bid"], row["Ask"], row["Market"], row["%Chg"],
                   row["Volume"], row["Type"], row["ITM"], row["Name"])

    # Produces all the html possible for an Option displayed in a group card
    # of the chain using just properties of the Option object
    def htmlInExpDateGroup(self, chopDuplicate = False, justPuts = False):
        bgITM = ""
        strikeSingle = ""
        strikeBoth = ""
        if self.itm:
            bgITM = "class='table-secondary'"
        if self.optionType == "put":
            strikeSingle = f"<td class='table-dark'>${self.strikePrice}</td>"
        if not chopDuplicate:
            strikeBoth = f"<td class='table-dark'>${self.strikePrice}</td>"
        if justPuts:
            strikeSingle = ""

        htmlStr = f"""
            {strikeSingle}
            <td {bgITM}>${self.bid}</td>
            <td {bgITM}>${self.ask}</td>
            <td {bgITM}>${self.market}</td>
            <td {bgITM}>{self.volume}</td>
            {strikeBoth}
        """
        return htmlStr
# Represents a group of Options that all Expire on the same day for easier
# accordian card rendering (cards are by expiration date)
class OptionEDG:
    _genID = 0
    def __init__(self, expDate, options):
        self.expDate = expDate
        self.options = options
        
        lenCalls = len(options["calls"]) if options.get("calls") else 0
        lenPuts = len(options["puts"]) if options.get("puts") else 0
        self.numContracts = lenCalls + lenPuts

        OptionEDG._genID += 1
        self.groupID = f"edg{OptionEDG._genID}"

    # Creates an OptionExpDateGroup from a list of call Option objects, put
    # Option objects, or both lists.
    @classmethod
    def fromOptionLists(cls, callList = None, putList = None):
        optionsDict = {}
        if callList is not None and putList is None:
            expDate = callList[0].expiration
            optionsDict["calls"] = callList
        elif putList is not None and callList is None:
            expDate = putList[0].expiration
            optionsDict["puts"] = putList
        else:
            expDate = callList[0].expiration
            optionsDict["calls"] = callList
            optionsDict["puts"] = putList
        return cls(expDate, optionsDict)

    # Produces the entire html for a expiration date group of contracts
    def htmlExpDateGroupCard(self):
        calls = self.options.get("calls")
        puts = self.options.get("puts")

        if calls is not None and puts is None:
            thead = """
                <tr>
                    <th colspan="5">Calls</th>
                </tr>
                <tr>
                    <th>Bid</th>
                    <th>Ask</th>
                    <th>Market</th>
                    <th>Volume</th>
                    <th><i>Strike</i></th>
                </tr>
            """
            rows = ""
            for option in calls:
                rows += f"""
                    <tr>
                        {option.htmlInExpDateGroup()}
                    </tr>
                """
        elif puts is not None and calls is None:
            thead = """
                <tr>
                    <th colspan="5">Puts</th>
                </tr>
                <tr>
                    <th>Bid</th>
                    <th>Ask</th>
                    <th>Market</th>
                    <th>Volume</th>
                    <th><i>Strike</i></th>
                </tr>
            """
            rows = ""
            for option in puts:
                rows += f"""
                    <tr>
                        {option.htmlInExpDateGroup(justPuts = True)}
                    </tr>
                """
        else:
            thead = """
                <tr>
                    <th colspan="4">Calls</th>
                    <th><i>Strike</i></th>
                    <th colspan="4">Puts</th>
                </tr>
                <tr>
                    <th>Bid</th>
                    <th>Ask</th>
                    <th>Market</th>
                    <th>Volume</th>
                    <th>↓↓</th>
                    <th>Bid</th>
                    <th>Ask</th>
                    <th>Market</th>
                    <th>Volume</th>
                </tr>
            """
            callsLen = len(calls)
            putsLen = len(puts)
            longerLen = callsLen if callsLen > putsLen else putsLen
            rows = ""
            for i in range(longerLen):
                if i >= callsLen:
                    rows += f"""
                        <tr>
                            <td colspan="4"></td>
                            {puts[i].htmlInExpDateGroup()}
                        </tr>
                    """
                elif i >= putsLen:
                    rows += f"""
                        <tr>
                            {calls[i].htmlInExpDateGroup()}
                            <td colspan="4"></td>
                        </tr>
                    """
                else:
                    rows += f"""
                        <tr>
                            {calls[i].htmlInExpDateGroup(chopDuplicate = True)}
                            {puts[i].htmlInExpDateGroup(chopDuplicate = True)}
                        </tr>
                    """

        # Now prepare html with customized table header and rows
        gid = self.groupID
        htmlStr = f"""
            <div class="card bg-light text-dark" id="card{gid}">
                <div class="card-header d-flex align-items-center">
                    <div class="p-1 w-100 align-middle">
                        Exp:&nbsp;{self.expDate}
                    </div>
                    <div class="p-1 flex-shrink-1 align-middle">
                        {self.numContracts}&nbsp;Contracts&nbsp;
                    </div>
                    <div class="p-1 flex-shrink-1 align-middle">
                        <button class="btn btn-dark collapsed" type="button" data-toggle="collapse" data-target="#collapse{gid}">
                            <span class="text-white" id="btn{gid}">
                                ↕
                            </span>
                        </button>
                    </div>
                </div>
                <div id="collapse{gid}" class="collapse" data-parent="#ocAccordian">
                    <div class="card-body text-center justify-content-center">
                        <table class="table table-sm">
                            <thead class="thead-light">
                                {thead}
                            </thead>
                            <tbody>
                                {rows}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        """
        return htmlStr

# Represents an entire Option Chain that is returned by the Options Chain API.
# Contains a dictionary of all the expriation date groups.
class OptionChain:
    def __init__(self, symbol, underlyingPrice, expDateGroups):
        self.symbol = symbol
        self.underlyingPrice = underlyingPrice
        self.expDateGroups = expDateGroups

    
    def htmlOCAccordian(self):
        script = """
            <script>
                $('#viewOptionChain').modal('show');
            </script>
        """
        title = f"""
            {self.symbol} Option Chain | 
            Underlying Price: ${self.underlyingPrice} | 
            {len(self.expDateGroups)} Expiry Date(s) |
            ITM = Grey
        """
        cards = """
            <div class="text-center text-muted">
                <i>
                    <u>NOTE:</u>
                    <br>
                    Due to variance in TD API data collection timing,
                    options with strikes very close to the underlying price may
                    be inaccurately deemed ITM/OTM when requested.
                </i>
            </div>
            <hr>
        """
        for edg in self.expDateGroups:
            cards += f"{edg.htmlExpDateGroupCard()}"
        oc = f"<div class='accordian' id='ocAccordian'>{cards}</div>"
        return {"script": script, "title": title, "oc": oc}