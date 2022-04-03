import os
from flask_mail import Mail, Message
import smtplib, ssl
from flask import Flask, render_template, request

app = Flask(__name__)


app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT '] = 587
app.config['MAIL_USERNAME'] = "nk_ahsn@hotmail.com"
app.config['MAIL_PASSWORD'] = "SKATEboard4life"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/", methods=["GET","POST"])
def main():

    is_register = False
    if request.method == "POST":
        user_name =  request.form.get('firstName')
        user_email = request.form.get('emailAddress')
        user_text =  request.form.get('longTextInput')

        is_register = True

        with mail.connect() as conn:
            subject = f"From: {user_name}-{user_email}"
            sender = "nk_ahsn@hotmail.com"
            msg = Message(
                subject=subject,
                body=user_text,
                sender=sender,
                recipients=["ahsnl.mi@gmail.com"]
            )
            conn.send(msg)
            return render_template('index.html', isRegister=is_register)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

