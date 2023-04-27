from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
from datetime import datetime
application = Flask(__name__, static_url_path='/static')


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/capture/')
def capture():
    return render_template('capture.html')


@application.route('/birdex/')
def birdex():
    df = db.get_switch()
    switch_frame = str(df.to_json())
    return render_template('birdex_list.html', switch_frame=switch_frame)


@application.route("/send_index", methods=["GET", "POST"])
def update():
    getIndex = int(request.form["maxIndex"]) + 1  # 모델 클래스에 비해 ???이 더해졌으므로 +1
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = f"UPDATE `birdex`.`birdex` SET `date` = '{date}', \
          `get_switch` = '1' WHERE (`no` = '{getIndex}');"
    db.update(sql)
    image = f"static/img/{getIndex}.jpeg"
    if os.path.isfile(image):
        os.remove(image)
    uploaded_files = request.files['image']
    uploaded_files.save(image)
    return redirect(url_for("index"))


@application.route('/birdex/content/<id_num>')
def birdex_content(id_num):
    id_num = int(id_num)
    birdex_series = db.birdex(id_num)
    photo = f"img/{id_num}.jpeg"
    if id_num == 0:
        id_num = '???'
    return render_template('birdex_content.html', id_num=id_num,
                           k_name=birdex_series['k_name'],
                           e_name=birdex_series['e_name'],
                           s_name=birdex_series['s_name'],
                           length=birdex_series['length'],
                           weight=birdex_series['weight'],
                           date=birdex_series['date'],
                           description=birdex_series['description'],
                           photo=photo
                           )


if __name__ == "__main__":
    application.run(debug=True)
    # application.run(host='0.0.0.0', debug=True, port=int(sys.argv[1]))
