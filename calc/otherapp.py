from __future__ import absolute_import

import contextlib
import urllib2

from flask import Flask, request
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SERVER_NAME='localhost:5002',
)


@app.route("/", methods=['GET'])
def index():
    return "Hello World! I'm an app that interfaces with the calc."

@app.route("/execute/<method>", methods=['GET'])
def nonsense(method):
    numbers = request.args.getlist('numbers')
    url = 'http://localhost:5001/{0}?numbers={1}'.format(method, numbers[0])
    print url
    req = urllib2.Request(url)
    with contextlib.closing(urllib2.urlopen(req, timeout=2)) as resp:
        print 3
        return resp.read(), resp.getcode()


if __name__ == "__main__":
    app.run()
