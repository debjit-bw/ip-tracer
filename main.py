import os
from flask import Flask, redirect, request, jsonify

hash_db = {
    "ooooo": "test",
    "sgwhl": "rishav",
    "wiurf": "smit",
    "euhgb": "god",
    "bihgs": "ayos",
    "dcwvg": "foyie",
    "bznru": "spark",
    "qqaer": "bhorchaj", 
    "iuqeg": "rick",
    "bwfyi": "june"
}

ip_db = {}

app = Flask(__name__)

@app.route('/')
def hello():
    name = hash_db[request.query_string.decode("utf-8")]
    if name == "test":
        return(jsonify(ip_db))
    ip_db[name] = str(request.remote_addr)
    return redirect("http://www.google.com", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)