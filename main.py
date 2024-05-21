from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):

    station_length = len(station)
    path = f"data/TG_STAID{station.zfill(6)}.txt"

    df = pd.read_csv(path, skiprows=20, parse_dates=["    DATE"])

    date_df = df.loc[df["    DATE"] == date]
    raw_temperature = date_df["   TG"]
    temperature = raw_temperature.squeeze() / 10

    if temperature == -999.9:
        temperature = "LOST"

    dictionary = {"station": station,
                  "date": date,
                  "temperature": temperature}

    return dictionary


if __name__ == "__main__":
    app.run(debug=True)
