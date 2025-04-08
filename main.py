from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mars_gallery():
    images = [
        {
            'filename': 'mars1.jpg',
            'title': 'Долины Маринера',
            'description': 'Крупнейший каньон в Солнечной системе'
        },
        {
            'filename': 'mars2.jpg',
            'title': 'Гора Олимп',
            'description': 'Самая высокая гора в Солнечной системе'
        },
        {
            'filename': 'mars3.jpg',
            'title': 'Равнина Эллада',
            'description': 'Ударный бассейн диаметром 2300 км'
        },
        {
            'filename': 'mars4.jpg',
            'title': 'Северная полярная шапка',
            'description': 'Состоит из водяного льда и замерзшего CO₂'
        }
    ]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)