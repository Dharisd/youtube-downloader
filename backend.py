from flask import Flask,request
import sys
app = Flask(__name__)




@app.route('/', methods=["POST"])
def recurl():
    data = request.form['url']
    #print("hello")
    print(data)
    return (data)


@app.route('/api/<path:link>', methods=["get"])
def geturl(link):
    data = link
    print("hello")
    print(data, file=sys.stderr)
    return (data)

 

 

        