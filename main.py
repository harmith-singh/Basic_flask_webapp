
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, and Hello world!"

app.run()
