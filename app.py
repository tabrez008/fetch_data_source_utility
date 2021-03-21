from flask import Flask, render_template
from gitutil import find_files
import os
from flask import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_data_sources", methods=["POST"])
def get_data_source():
    print(os.getcwd())
    result = find_files(os.getcwd() + "/src")
    response = app.response_class(
        response=json.dumps(result), status=200, mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)