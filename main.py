import os
from flask import Flask, redirect, request, jsonify

hash_db = {}
redirex_db = {}
ip_db = {}

app = Flask(__name__)

@app.route('/')
def hello():
    global hash_db
    global redirex_db
    name = hash_db[request.query_string.decode("utf-8")]
    ip_db[name] = str(request.remote_addr)
    return redirect(redirex_db[name], code=302)

@app.route('/internal/hashing')
def dbmake():
    global hash_db
    link = request.query_string.decode("utf-8").split('@')
    #   hashing?giubkw@rishav
    if link[0] == "flush":
        if link[1] == "flush":
            hash_db = {}
            return(jsonify(hash_db))
        else:
            del hash_db[link[1]]
            return(jsonify(hash_db))
    hash_db[link[0]] = link[1]
    return(jsonify(hash_db))

@app.route('/internal/redirection')
def redirex():
    global redirex_db
    link = request.query_string.decode("utf-8").split('@')
    #   redirection?rishav@https://www.youtube.com
    if link[0] == "flush":
        if link[1] == "flush":
            redirex_db = {}
            return(jsonify(redirex_db))
        else:
            del redirex_db[link[1]]
            return(jsonify(redirex_db))
    redirex_db[link[0]] = link[1]
    return(jsonify(redirex_db))

@app.route('/admin/june-hunting')
def iplister():
    global ip_db
    pw = request.query_string.decode("utf-8")
    if pw == "beeplovesjune":
        return(jsonify(ip_db))
    else:
        return("u an imposter. enter the truth.")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)