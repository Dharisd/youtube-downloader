from flask import Flask,request,jsonify,render_template
import sys
from youtube_dl import YoutubeDL
import json
import random
import urllib.request
app = Flask(__name__)


def dl_link(dll):
    print(dll)
    jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer',
                       'method':'aria2.addUri',
                       'params':[[dll]]})

    c = urllib.request.urlopen('http://127.0.0.1:6800/jsonrpc', jsonreq.encode('utf-8'))



def get_formats(url): 
    with YoutubeDL() as ydl:
        links = {}
        dl = ydl.extract_info(url, download=False)
        formats = dl['formats']
        for i in range(0,len(formats)):
            typ = formats[i]["ext"]
            if (typ == "mp4"):
                #print(formats[i]["format_id"]+ " "+ formats[i]["format_note"])
                links[formats[i]["format_note"]] = formats[i]["url"]
        return links









@app.route('/', methods=["GET","POST"])
def serve():
    return render_template("index.html")


@app.route('/url', methods=["POST"])
def recurl():
    data = request.form['url']
    #print("hello")
    print(data)
    qlty = get_formats(data)
    aql = json.dumps(qlty)
    #print (aql)

    return (jsonify(qlty))

@app.route("/download", methods=['POST'])
def submit():
    data = dict(request.headers)
    print(data["Urlv"])
    dl_link(data["Urlv"])
    return('success')
    
    


