from flask import Flask, jsonify
from flask_cors import CORS

# Config
DEBUG = True

# Create app instance

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/ping")
def ping_pong():
    return jsonify("pong!")cd 


if __name__ == "__main__":
    app.run()
