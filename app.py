from flask import Flask, render_template, request, session, redirect, url_for
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для работы с сессиями

# Инициализация Flask-Babel
babel = Babel()

# Функция для выбора языка
def get_locale():
    return session.get('lang', 'en')  # Возьмем язык из сессии (или используем 'en' по умолчанию)

babel.init_app(app, locale_selector=get_locale)  # Подключаем Babel к приложению с функцией выбора языка

@app.route("/")
def home():
    return render_template("index.html", get_locale=get_locale)  # Отображаем главную страницу

@app.route("/about")
def about():
    return render_template("about.html", get_locale=get_locale)  # Страница "О нас"

@app.route("/dayz-server")
def dayz_server():
    return render_template("dayz_server.html", get_locale=get_locale)  # Страница сервера DayZ
@app.route("/oldsg")
def oldsg():
    return render_template("oldsg.html", get_locale=get_locale)     # Страница канала

@app.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    next_url = request.referrer or url_for('home')  # Возвращаем пользователя на предыдущую страницу или на главную
    return redirect(next_url)

if __name__ == "__main__":
    app.run(debug=True)  # Запуск приложения
