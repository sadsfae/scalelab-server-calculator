#!/usr/bin/env python
# flask app to calculate cost of servers

from flask import Flask, request, redirect, render_template, url_for
from flaskext.htmlbuilder import html, render

app = Flask(__name__)

import os
import sys

# render default HTML index
@app.route("/")
def index():
    return render_template('index.html')

# calculate price of servers + cabling and 2 x 10GbE ports
def addserver(servers):
    servers = int(servers)
    serverunitcost = 5800
    cablecost = 50
    priceperport = 230
    portcost = priceperport * 2
    return (serverunitcost + cablecost + portcost) * servers

# take the results of server query and post them
@app.route("/post_server_total", methods=["post"])
def addserverpost():
    "post input for server total"
    servers = request.form['servers']
    txt = render([
        html.doctype('html'),
        html.html(lang='en')(
            html.head(
                html.title('Scalelab Server Calculator 5000')
            ),
            html.body(
                "%s Dell R620 node(s) with cabling, 2 x 10gbe ports (20GbE in/out) will cost $%s USD" \
                        % (servers,addserver(servers))
                )
            )
        ])

    return txt

if __name__ == '__main__':
    app.run
