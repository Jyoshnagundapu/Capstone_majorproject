import smtplib
from email.message import EmailMessage
import json
def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data= json. load (json_file)
    return data
def SendMailToCustomer():
    filepath_VoiceAssistant='output1.json'
    customer_data=read_json_file(filepath_VoiceAssistant)
    customer_email=customer_data['email']
    customer_name=customer_data['name']
    mobile=customer_data['mobile_no']
    summary=customer_data['summary']
    problem=customer_data['problem']
    customer_service=customer_data['customer_service']
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    msg = EmailMessage()
    msg['Subject'] = f'{problem}-{customer_name}'
    msg['From'] = customer_email
    msg['To'] = f'{customer_service}'
    msg.set_content(f'''
        <html>
            <body style="color: black;"
            <p>Hi {problem} Resolver Team,</p>
            <p>We got a new request from a customer(mentioned details below) and below is the description of the problem:</p>
            <ul>
                    <li><b>Name of the customer</b>-{customer_name}</li>
                    <li><b>Issue</b>-{summary}</li>
                    <li>Incase of more details please contact-{mobile}</li>

            </ul>
            <p>Please feel free to contact to the customer in case of any queries</p>
            <p>Thank you in advance!</p>
            <br>
            <p>Best Regards,<br>
            Customer Support Team</p>
        </body>
        </html>
        ''',subtype='html')
    
    email_address="vendordatamaintenance@gmail.com"
    email_password="abetyywjxfjciwuu"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        smtp.quit()

SendMailToCustomer()






