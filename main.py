from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 12
    dictionary = [{"station": station, "date": date, "temperature": temperature}]
    return dictionary


if __name__ == "__main__":
    app.run(debug=True)