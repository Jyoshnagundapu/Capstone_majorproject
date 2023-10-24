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
    ticket_number=customer_data['ticket-id']
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    msg = EmailMessage()
    msg['Subject'] = 'Customer Request Update'
    msg['From'] = 'vendordatamaintenance@gmail.com'
    msg['To'] = f'{customer_email}'
    msg.set_content(f'''
        <html>
            <body style="color: black;"
            <p>Hi {customer_name},</p>
            <p>Your request has been successfully registered, and we have created a ticket to track its progress. Below are the details of your request:</p>
            <ul>
                    <li><strong>Ticket Number:</strong> {ticket_number}</li>
            </ul>
            <p>We will get back to you shortly with updates on your request.</p>
            <p>Thank you for using our services!</p>
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






