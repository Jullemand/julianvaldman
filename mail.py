from types import LambdaType
import requests
import os

class Mail():

    def __init__(self) -> None:
        self.domain_name = os.environ.get("MAILGUN_DOMAIN")
        self.api_key = os.environ.get("MAILGUN_API")
        self.mail_receiver = ["julian_1108@hotmail.com"]

    def send_simple_message(self):

        print(f"https://api.mailgun.net/v3/{self.domain_name}/messages")

        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain_name}/messages",
            auth=("api", self.api_key),
            data={"from": f"Portfolio Page <mailgun@{self.domain_name}>",
                "to": self.mail_receiver,
                "subject": "Hello",
                "text": "Testing some Mailgun awesomness!"})

    def send_contact_mail(self, payload):

        name = payload['name']
        subject = payload['subject']
        email = payload['email']
        message = payload['message']

        text = f"""
Name    :  {str(name)}
Email   :  {str(email)}
Subject :  {str(subject)}
Message :  {str(message)}
"""

        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain_name}/messages",
            auth=("api", self.api_key),
            data={  "from": f"Portfolio Page <mailgun@{self.domain_name}>",
                    "to": self.mail_receiver,
                    "subject": "Contact",
                    "text": text})


if __name__ == "__main__":

    a = os.environ.get("MAILGUN_API")
    print(a)

    mail = Mail()
    res = mail.send_simple_message()
    print(res)

    """
    OLD: Python Mail Service

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
    
    """