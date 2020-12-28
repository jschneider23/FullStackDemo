import os

def clearOldGraphs():
    files = [f for f in os.listdir("frontend/graphs") if f.endswith(".html")]
    for f in files:
        os.remove(os.path.join("frontend/graphs", f))