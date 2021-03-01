# This file contains auxiliary functions for the Flask app
import os

# Clears chart files still in the charts directory from previous profile 
# modal loads
def clearOldCharts():
    files = [f for f in os.listdir("frontend/charts") if f.endswith(".html")]
    for f in files:
        os.remove(os.path.join("frontend/charts", f))