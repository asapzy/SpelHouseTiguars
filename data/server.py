from flask import Flask

import os
from sodapy import Socrata
from dotenv import load_dotenv
from flask import Flask
import pandas as pd
import json

load_dotenv()
token = os.getenv("APP_TOKEN")
# "https://data.sfgov.org/resource/5xmc-5bjj.json"

domain = "data.sfgov.org"
prefix = "https://"
identifier = "5xmc-5bjj"

client = Socrata(domain, token)
results = client.get(identifier)
df = pd.DataFrame(results)
mapData = dict(df['the_geom'])


app = Flask(__name__)

@app.route("/data")
def data():
    data = json.dumps(mapData)
    return(data)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    # app.run(debug=True)