import urllib2, json
jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer',
                       'method':'aria2.addUri',
                       'params':[['https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe']]})

c = urllib2.urlopen('http://127.0.0.1:6800/jsonrpc', jsonreq.encode('utf-8'))