from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

# Создаем главную страницу с формой ввода имени и электронной почты
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Обрабатываем отправку формы
@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные из формы
    name = request.form['name']
    email = request.form['email']

    # Создаем cookie с данными пользователя
    response = make_response(redirect('/welcome'))
    response.set_cookie('name', name)
    response.set_cookie('email', email)

    return response

# Создаем страницу приветствия, где отображается имя пользователя
@app.route('/welcome', methods=['GET'])
def welcome():
    # Получаем данные пользователя из cookie
    name = request.cookies.get('name')

    return render_template('welcome.html', name=name)

# Обрабатываем нажатие на кнопку "Выйти"
@app.route('/logout', methods=['GET'])
def logout():
    # Удаляем cookie с данными пользователя и перенаправляем на страницу ввода
    response = make_response(redirect('/'))
    response.set_cookie('name', expires=0)
    response.set_cookie('email', expires=0)

    return response

if __name__ == '__main__':
    app.run(debug=True)


