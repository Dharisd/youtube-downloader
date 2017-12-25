from flask import Flask,request
import sys
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])


def geturl():
    data = request.data
    print("hello")
    print(data, file=sys.stderr)
    return "data"

 

        