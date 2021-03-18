# This file contains auxiliary functions for the backend

from backend import bd_config as cfg
from datetime import datetime as dt

# Formats the value of an attribute to have necessary symbols before or after
# the value, such as $ <value> for money amounts or <value> % for percentages.
# Also handles rounding and date formatting.
# This applies to any data on frontend that will use data from one of the two
# functions above.  Does not apply to movers as this requires extra formatting.
def attrFormat(sym, attr, value):
    # Format Datetime into format "Jan 1 2020".  Returns early as no other
    # formatting is required if the value is for divDate.
    if attr == "divDate":
        if value != "":
            value = str(value[:value.index(" ")])
            dtObj = dt.strptime(value, "%Y-%m-%d")
            return dtObj.strftime("%b %d %Y")
        else:
            return "No Dividends"
    # Attributes that need rounding (regardless of whether index or stock)
    # The nested if statement appends a 0 if a value has a decimal only to
    # the tenths place so that the values make sense in context (ex: instead
    # of $1,234.5 and 12.0%, they will be $1,234.50 and 12.00%).  The format
    # function messes with the extra 0, so it is used twice to ensure proper
    # display.
    if attr in cfg.roundedAttrs:
        value = "{:.2f}".format(float(value))
        if len(value[value.index("."):]) == 2:
            value = f"{value}0"
    # Attributes that need commas added between thousands for readability
    if attr in cfg.commaAttrs:
        if "." in str(value):
            if str(value) != "0.00":
                value = "{:,}".format(float(value))
            if len(value[value.index("."):]) == 2:
                value = f"{value}0"
        else:
            value = "{:,}".format(int(value))
    # Attributes that need a % afterhand
    if attr in cfg.percentAttrs:
        value = f"{value}%"
    # Attributes that need a $ beforehand
    if "$" not in sym and attr in cfg.moneyAttrs:
        value = f"${value}"
    return value