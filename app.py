from flask import Flask, request
import json

import db

app = Flask(__name__)


@app.route('/')
def helloWorld():
    response = {"status": "Message received"}
    print("Sending data")
    return json.dumps(response)


@app.route('/signup', methods = ['POST'])
def signUp():
    response = {}
    info = request.get_json()

    status = db.signUp(info)

    return json.dumps(db.response_codes[status])





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
