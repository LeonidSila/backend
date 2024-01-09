
# Импорт необходимых модулей
from flask import Flask, render_template

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Маршрут для домашней страницы
@app.route('/')
def home():
    return render_template('home.html')

# Маршрут для страницы «одежда»
@app.route('/clothing.html')
def clothing():
    return render_template('clothing.html')

# Маршрут для страницы «обувь»
@app.route('/shoes.html')
def shoes():
    return render_template('shoes.html')

# Маршрут для страницы «куртка»
@app.route('/jacket.html')
def jacket():
    return render_template('jacket.html')


@app.route('/kek.html')
def kek():
    return render_template('kek.html')

@app.route('/images')
def images():
    return render_template('')

if __name__ == '__main__':
    app.run(debug=True)


