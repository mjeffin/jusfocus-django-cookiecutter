import requests
from django.conf import settings

def send_simple_message(subject,text_message,to_email_ids=[],from_mail_id="JusLaw <admin@mail.juslaw.in>"):
    """
    eg: send_simple_message(subject="Hello",text_message="Testing!",to_email_ids=("admin@jusfocus.com"),from_mail_id)  

    ## Parameters:
    to_email_ids:list of reciever's mail id
    subject: String
    text_message: String
    from_mail_id: default from_mail_id=JusLaw <admin@mail.juslaw.in>
                from_mail_id = f"Teacher <teacher@{MAILGUN_DOMAIN_NAME}>"

    ## Returns
        mailgun api response
    """
    MAILGUN_DOMAIN_NAME=settings.ANYMAIL['MAILGUN_SENDER_DOMAIN']
    MAILGUN_API_KEY=settings.ANYMAIL['MAILGUN_API_KEY']
    #from_mail_id = f"Teacher <teacher@{MAILGUN_DOMAIN_NAME}>"
    return requests.post(
        f"https://api.eu.mailgun.net/v3/{MAILGUN_DOMAIN_NAME}/messages",
        auth=("api", f"{MAILGUN_API_KEY}"),
        data={"from": from_mail_id,
              "to": to_email_ids,
              "subject": subject,
              "text": text_message})