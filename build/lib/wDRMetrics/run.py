from pyDRMetrics.pyDRMetrics import *
import os, sys, json, uuid
from flask import Flask, render_template, request
import uuid

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # limit to 5MB

# routes
@app.route("/", methods=['GET'])
def dr():
	return render_template("dr.html")

@app.route("/drx", methods=['GET'])
def drx():
	return render_template("drx.html")

@app.route("/about")
def about():
	return "Created by Dr. Zhang (oo@zju.edu.cn)"

@app.route("/dr", methods = ['POST'])
def run_dr(save_local = False):
	
    use_sample = int(request.form["use_sample"])
    path = ""
    if (use_sample == 1):
        path = os.path.dirname(os.path.realpath(__file__)) + "/static/digits.csv"
    elif (use_sample == 2):
        path = os.path.dirname(os.path.realpath(__file__)) + "/static/raman.csv"
    elif (use_sample == 3):
        path = os.path.dirname(os.path.realpath(__file__)) + "/static/cancer.csv"
    else:
        f = request.files['dataFile']
        path = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".csv"
        f.save(path)

    k = int(request.form["n_components"])
    dr = request.form["dr"]
    drm = DRMetrics.test(path, k, dr)

    if save_local:
        fn = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".html"
        with open(fn, 'w') as f:
            f.write()

        print(fn)
    
    return {'message': 'success', 'html': drm.get_html()} 

@app.route("/drx", methods = ['POST'])
def run_drx(save_local = False):

    fX = request.files["csvX"]
    fZ = request.files["csvZ"]
    fXr = request.files["csvXr"]

    csvX = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".csv"
    fX.save(csvX)
    csvZ = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".csv"
    fZ.save(csvZ)
    csvXr = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".csv"
    fXr.save(csvXr)

    drm = DRMetrics.from_files(csvX, csvZ, csvXr)

    if save_local:
        fn = os.path.dirname(os.path.realpath(__file__)) + "/" + str(uuid.uuid4()) + ".html"
        with open(fn, 'w') as f:
            f.write()

        print(fn)
    
    return {'message': 'success', 'html': drm.get_html()} 

'''
The Flask dev server is not designed to be particularly secure, stable, or efficient. 
By default it runs on localhost (127.0.0.1), change it to app.run(host="0.0.0.0") to run on all your machine's IP addresses.
0.0.0.0 is a special value that you can't use in the browser directly, you'll need to navigate to the actual IP address of the machine on the network. You may also need to adjust your firewall to allow external access to the port.
The Flask quickstart docs explain this in the "Externally Visible Server" section:
    If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.
    If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line.
'''

import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://localhost:5006/')
      
if __name__ =='__main__':
    # use netstat -ano|findstr 5006 to check port use
    Timer(3, open_browser).start()
    app.run(host="0.0.0.0", port=5006, debug = True)
    