from flask import Flask, request, make_response, redirect, render_template, flash
from app.config import Config
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.forms import Persona
from flask_mail import Mail, Message


app = create_app()
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'orlandoflutter@gmail.com'
app.config['MAIL_PASSWORD'] = 'dcrdjpgdaglchyue'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

app.secret_key = "F3YEFgqBw:0%p\~mSF"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    form = Persona()
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        asunto = request.form.get('asunto')
        mensaje = request.form.get('mensaje')

        msg = Message(subject=f"Correo de{nombre}", body=f"Email: {correo}\n Telefono: {telefono}\n Asunto: {asunto}\n\n\n{mensaje}", sender='martinez17v@gmail.com', recipients=['orlandoflutter@gmail.com'])
        mail.send(msg)
        # success = "Mensaje enviado"

    return render_template('form.html', form= form)

def main():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    return app
