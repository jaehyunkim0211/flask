from flask import Flask
app = Flask(__name__)


@app.route("/model/lstm", methods=["POST"])
def lstm():
    return "lstm 값"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
