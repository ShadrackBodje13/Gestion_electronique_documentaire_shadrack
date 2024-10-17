import os
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ocr_classification import process_file
import smtplib

def move_file(src, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)  # Assure that the directory exists
    shutil.move(src, dest)

def send_notification(email_recipient, email_sender, smtp_info, subject, message):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_info['server'], smtp_info['port'])
    server.starttls()
    server.login(email_sender, smtp_info['password'])
    server.sendmail(email_sender, email_recipient, msg.as_string())
    server.quit()

def main(file_path, email_recipient, email_sender, smtp_info):
    base_filename = os.path.splitext(os.path.basename(file_path))[0]
    doc_type = process_file(file_path)  # This function must return the document type
    new_filename = f"{doc_type}_{base_filename}.pdf"
    output_folder = 'output_folder'
    new_file_path = os.path.join(output_folder, new_filename)

    move_file(file_path, new_file_path)

    message = f"Your document {new_filename} has been processed and classified."
    subject = "Document Processing Complete"
    send_notification(email_recipient, email_sender, smtp_info, subject, message)

if __name__ == "__main__":
    email_sender = 'example@example.com'
    email_recipient = 'recipient@example.com'
    smtp_info = {
        'server': 'smtp.example.com',
        'port': 587,
        'password': os.getenv('EMAIL_PASSWORD')
    }
    file_path = '/path/to/input_documents/document.pdf'
    main(file_path, email_recipient, email_sender, smtp_info)
