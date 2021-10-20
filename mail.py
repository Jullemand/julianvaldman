from types import LambdaType
import requests

class Mail():

    def __init__(self) -> None:
        self.domain_name = "sandbox2e7b8ad2e9034b0980ec7978af638425.mailgun.org"
        self.test_domain_name = "samples.mailgun.org"
        # self.api_key = "2bf328a5-f42f3eb0"
        self.api_key = "120798de5eac5cc2a0a2cd6d7d0c8151-2bf328a5-f42f3eb0"

    def send_simple_message(self):

        print(f"https://api.mailgun.net/v3/{self.domain_name}/messages")

        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain_name}/messages",
            auth=("api", self.api_key),
            data={"from": f"Portfolio Page <mailgun@{self.domain_name}>",
                "to": ["julian_1108@hotmail.com"],
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
                    "to": ["julian_1108@hotmail.com"],
                    "subject": "Contact",
                    "text": text})


if __name__ == "__main__":

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