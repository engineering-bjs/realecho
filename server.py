import os
import sys
import json

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/", methods=["GET", "PUT", "POST", "DELETE", "OPTIONS"])
@app.route("/<path>", methods=["GET", "PUT", "POST", "DELETE", "OPTIONS"])
def echo(**kwargs):
    rdata = {
        "body": request.data,
        "args": request.args,
        "form": request.form,
        "headers": dict(request.headers),
        "path": request.path
    }
    print(rdata)

    if os.getenv("PPRINT_JSON"):
        print(json.dumps(json.loads(request.data.decode("utf-8")), indent=2, sort_keys=True))

    sys.stdout.flush()

    return make_response("200 OK", 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
