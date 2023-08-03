import os
import smtplib
from email.message import EmailMessage
import imghdr
import csv
from verify_email import verify_email

EMAIL_ADDRESS = os.environ.get("Email_IITBHU")
EMAIL_PASS = os.environ.get('Email_IITBHU_Pass')

def personalised_message(to, name=None):
    msg = EmailMessage()
    msg['Subject'] = """Invitation to Participate in Water Rocket Event "Momentum" at Technex'23"""
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg.set_content("""Hello! Greetings from Technex IIT-BHU,

    We hope this email finds you well. Being a member of the organizing team of Technex'23, the technical fest of IIT-BHU, We are pleased to invite you to participate in our exciting water rocket event "Momentum".

    "Momentum" is a thrilling competition that challenges your creativity and technical skills to design and launch a water-powered rocket. The event aims to promote innovation and teamwork, and it promises to be a fun-filled experience for all participants.
    So are you ready for a blast of fun and learning? Using just a plastic bottle, water, and a pump,you'll build and launch your own water rocket and see how high and far your creation can soar into the sky. Your water rocket launch will be judged, and the farthest launches will be awarded. Not only will you have a blast, but you'll also learn valuable skills that will challenge your mind and broaden your horizons.
    So, grab your team and let's launch into action!

    The event will take place on Mar 17-19 at the IIT-BHU campus. You and your team are required to design and build a rocket that can fly the highest and farthest distance.

    Registrations are open at technex.co.in

    Thanks and regards
    Team Momentum
    Technex , IIT BHU""")

    path_img = 'Momentum.jpg'
    path_pdf = 'Momentum ps-1.pdf'

    with open(path_img, 'rb') as imgg:
        file_data = imgg.read()
        file_type = imghdr.what(imgg.name)
        file_name = imgg.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with open(path_pdf, 'rb') as pdff:
        file_data = pdff.read()
        file_name = pdff.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    return msg

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    with open('test.csv') as filee:
        data = csv.reader(filee)
        for email in data:
            is_valid = verify_email(email)
            if is_valid:
                smtp.send_message(personalised_message(email))
                print("message sent to ", email)
            else:
                print("message not sent to ", email)
                with open('notsent.csv', 'a') as notsent:
                    notsent.write(email[0]+',\n')