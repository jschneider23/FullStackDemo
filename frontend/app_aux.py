# This file contains auxiliary functions for the Flask app
import os

# Clears chart files still in the graphs directory from previous profile 
# modal loads
def clearOldGraphs():
    files = [f for f in os.listdir("frontend/graphs") if f.endswith(".html")]
    for f in files:
        os.remove(os.path.join("frontend/graphs", f))