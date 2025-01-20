from flask import Flask, render_template, session, redirect, url_for
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для работы с сессиями

# Инициализация Flask-Babel
babel = Babel()

# Функция для выбора языка
def get_locale():
    return session.get('language', 'ru')  # Возьмем язык из сессии (или используем 'ru' по умолчанию)

# Инициализация Flask-Babel с использованием функции get_locale для выбора языка
babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def home():
    return render_template("index.html", get_locale=get_locale)  # Отображаем главную страницу

@app.route("/about")
def about():
    return render_template("about.html", get_locale=get_locale)  # Страница "О нас"

@app.route("/dayz-server")
def dayz_server():
    return render_template("dayz_server.html", get_locale=get_locale)  # Страница сервера DayZ

@app.route("/set_language/<lang>")
def set_language(lang):
    if lang in ['ru', 'en']:
        session['language'] = lang  # Сохраняем выбранный язык в сессии
    return redirect(url_for('home'))  # Перенаправляем на главную страницу

if __name__ == "__main__":
    app.run(debug=True)  # Запуск приложения
