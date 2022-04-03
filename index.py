import os
from flask_mail import Mail, Message
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

load_dotenv()  # take environment variables from .env.
email_address = os.getenv('EMAIL_ADDR') 
email_pass = os.getenv('EMAIL_PASS')
sec_pass = os.getenv('FLASK_API_KEY') 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = sec_pass
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT '] = 587
app.config['MAIL_USERNAME'] = email_address
app.config['MAIL_PASSWORD'] = email_pass
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
db = SQLAlchemy(app)

class UserQueryContact(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    text_message = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, text_message):
        self.name = name
        self.email = email
        self.text_message = text_message

    def __repr__(self):
        return "<UserQueryContact(id='%s')>" % self.id

@app.route("/", methods=["GET","POST"])
def main():
    sender = email_address
    is_register = False
    if request.method == "POST":
        is_register = True
        user_name =  request.form.get('firstName')
        user_email = request.form.get('emailAddress')
        user_text =  request.form.get('longTextInput')

        subject = f"From: {user_name} |Email: {user_email}"
        # if not send_mail(sender, subject, user_text):
        new_query = UserQueryContact(user_name, user_email, user_text)
        db.session.add(new_query)
        db.session.commit()
            
        return render_template('index.html', isRegister=is_register)

    return render_template('index.html')

def send_mail(sender, subject, msg_body):
    try:
        with mail.connect() as conn:
            msg = Message(
                subject=subject,
                body=msg_body,
                sender=sender,
                recipients=["ahsnl.mi@gmail.com"]
            )
            conn.send(msg)
    except:
        return False

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=False)

