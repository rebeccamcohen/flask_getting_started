from flask import Flask, jsonify, request
import math
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def get_name():
    d = {
        "name": "Rebecca"
    }
    return jsonify(d)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    d = {
      "message": "Hello there, {}".format(name)
    }
    return jsonify(d)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    print(r)
    dist = math.sqrt(((r["a"][0] - r["b"][0])**2)+((r["a"][1] - r["b"][1])**2))
    d = {
        "distance": dist,
        "a": r["a"],
        "b": r["b"],
    }
    return jsonify(d)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
