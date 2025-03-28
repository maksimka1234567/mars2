from flask import Flask, render_template, url_for, request

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')