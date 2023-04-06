﻿from flask import Flask, render_template
import pandas as pd
import database as db

birdex = pd.DataFrame(db.rows)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture/')
def capture():
    return render_template('capture.html')

@app.route('/birdex/')
def birdex():
    return render_template('birdex_list.html')

if __name__ == '__main__':
    app.run(debug=True)