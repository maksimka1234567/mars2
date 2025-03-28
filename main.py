from flask import Flask, render_template, url_for, request
import json
import random
import os

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title: str):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof: str):
    prof = prof.lower()
    params = {'is_engineer': 'инженер' in prof or 'строитель' in prof, 'science_img_url': url_for(
        'static', filename='img/science_map.jpg'), 'engineer_img_url': url_for(
        'static', filename='img/engineer_map.jpg')}
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_of_professions(list):
    if list != 'ol' and list != 'ul':
        return "Неверный параметр"
    params = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
               'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
               'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list.html', params=params, param=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего', 'profession': 'штурман марсохода',
              'gender': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': True, 'style_url': url_for('static', filename='css/main.css')}
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('double security.html')
    elif request.method == "POST":
        return "Доступ открыт"


@app.route('/distribution')
def distribution():
    params = {'astronauts': ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
         'Венката Капур', 'Тедди Сандерс', 'Шон Бин']}
    return render_template('distribution.html', **params)


@app.route('/table/<gender>/<int:age>')
def table_param(gender, age):
    params = {'gender': gender, 'age': age, 'child_img_url': '/static/img/child.jpg', 'adult_img_url': '/static/img/adult.jpg',
              'style_url': url_for('static', filename='css/table.css')}
    return render_template('table.html', **params)


images_folder = os.path.join(os.getcwd(), 'static', 'landscapes')
image_files = [
    f'static/landscapes/{f}'
    for f in os.listdir(images_folder)
    if os.path.isfile(os.path.join(images_folder, f))
]
count = len(image_files) + 1


@app.route('/gallery', methods=["GET", "POST"])
def gallery():
    global count
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'static/landscapes/landscape{count}.png')
        image_files.append(f'static/landscapes/landscape{count}.png')
        count += 1
    return render_template('gallery.html', landscapes=image_files, count=count)


@app.route('/member')
def member():
    with open("members.json", "rt", encoding="utf8") as f:
        members_list = json.loads(f.read())
    member = random.choice(members_list["members"])
    member["about"] = ", ".join(sorted(member["about"]))
    return render_template('members.html', member=member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')