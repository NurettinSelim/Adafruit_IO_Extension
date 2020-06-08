from flask import Flask, render_template
from Adafruit_IO import Client, Data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:username>/<string:key>/yatak_odasi_isik/ALL_ON")
def all_on(username, key):
    aio = Client(username, key)

    feeds_key = ["yatak-odasi-isik1", "yatak-odasi-isik2", "yatak-odasi-isik3"]
    data = Data(value="ON")

    for feed_key in feeds_key:
        aio.create_data(feed_key, data)

    return("All the lights in the bedroom turned on")


@app.route("/<string:username>/<string:key>/yatak_odasi_isik/ALL_OFF")
def all_off(username, key):
    aio = Client(username, key)

    feeds_key = ["yatak-odasi-isik1", "yatak-odasi-isik2", "yatak-odasi-isik3"]
    data = Data(value="OFF")

    for feed_key in feeds_key:
        aio.create_data(feed_key, data)

    return("All the lights in the bedroom turned off")


if __name__ == "__main__":
    app.run(debug=True)
