from flask import Flask, render_template, request
import database as db
from datetime import datetime

def birdex_content():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Document</title>
        </head>
        <body>
            
        </body>
        </html>
"""

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture/')
def capture():
    return render_template('capture.html')

@app.route('/birdex/')
def birdex():
    df = db.get_switch()
    switch_frame = str(df.to_json())
    return render_template('birdex_list.html', switch_frame=switch_frame)

@app.route("/send_index", methods = ["post"])
def update():
    getIndex = request.get_json() + 1 # 모델 클래스에 비해 ???이 더해졌으므로 +1
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = f"UPDATE `birdex`.`birdex` SET `date` = '{date}', `get_switch` = '1' WHERE (`no` = '{getIndex}');"
    db.update(sql)
    return "TODO"
    
@app.route('/birdex/content/')
def birdex_content():
    df = db.get_switch()
    switch_frame = df.to_json()
    return render_template('birdex_content.html', switch_frame=switch_frame)

if __name__ == '__main__':
    app.run(debug=True)