from flask import Flask, render_template, url_for

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
    params = ['Инженер-исследователь', "Пилот", "Строитель", "Экзобиолог", "Врач", "Климатолог"]
    return render_template('list.html', params=params, param=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')