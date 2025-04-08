from flask import Flask, render_template
import json
import random

app = Flask(__name__)


@app.route('/member')
def member():
    # Загружаем данные из JSON файла
    with open('templates/crew_members.json', 'r', encoding='utf-8') as f:
        crew_data = json.load(f)

    # Выбираем случайного члена экипажа
    random_member = random.choice(crew_data['crew'])

    # Передаем данные в шаблон
    return render_template('member.html', member=random_member)


if __name__ == '__main__':
    app.run()