import os
from flask_mail import Mail, Message
from flask import Flask, render_template, request
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()  # take environment variables from .env.
email_address = os.getenv('EMAIL_ADDR') 
email_pass = os.getenv('EMAIL_PASS')
sec_pass = os.getenv('FLASK_API_KEY') 

app.config['SECRET_KEY'] = sec_pass
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

