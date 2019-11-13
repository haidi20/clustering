from flask import Flask

from Main import Main 

app = Flask(__name__)

@app.route('/')
def index():
    return Main.index()

app.run(debug=True, host='localhost', port= 8000)