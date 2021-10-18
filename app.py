'''
HOW TO SET UP FLASK

1) In terminal
    1.1) set FLASK_APP=app.py
    1.2) set FLASK_ENV=development
2) Run Flask - in terminal: flask run

'''

'''
WHAT I HAVE DONE TO MAKE THE TEMPLATE WORK

- Made 2 folders: "templates" and "static"
- I have inserted the "index.html" file in "templates"
- I have inserted all dependency folders: css, images, js and scripts in "static"
- I have created a Python file: app.py
- In index file, I have:
    - Added url_open when having a path refering to one of the 4 dependency folder - dynamic referencing to "static" folder
    - Removed version referencing like: ?ver=1.1.0
'''

'''
TODOs

- Set up email - /sendemail/ -> Use Mailgun??
- Change all texts
- Link to Linkedin and Github
- Add hobbies, events and courses
- Buy a domain

'''


from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, url_for, redirect

def create_app():

    # Has to be this name 
    # Then deployment mechanism will only deploy this app and MongoClient ONCE

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    @app.route("/sendemail/", methods=['POST'])
    def sendemail():
        if request.method == "POST":
            name = request.form['name']
            subject = request.form['Subject']
            email = request.form['_replyto']
            message = request.form['message']

            your_name = "Julian Valdman"
            your_email = "julian.val123@gmail.com"
            your_password = "valdman11"

            # Logging in to our email account
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(your_email, your_password)

            # Sender's and Receiver's email address
            sender_email = "julian.val123@gmail.com"
            receiver_email = "julian_1108@hotmail.com"

            msg = EmailMessage()
            msg.set_content("First Name : "+str(name)+"\nEmail : "+str(email)+"\nSubject : "+str(subject)+"\nMessage : "+str(message))
            msg['Subject'] = 'New Response on Personal Website'
            msg['From'] = sender_email
            msg['To'] = receiver_email
            # Send the message via our own SMTP server.
            try:
                # sending an email
                server.send_message(msg)
            except:
                pass
        
        return redirect('/#contact');

    return app
