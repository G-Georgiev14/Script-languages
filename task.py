import smtplib
from email.mime.text import MIMEText

email_address = "Моят имейл"
email_password = "Паролата"  
to_email = "Вашият имейл"  

body = f"Не пропускай шанса си! Само днес – всички продукти с до 50% намаление. Купи сега, докато количествата стигнат! 🛒🔥“\nГеорги Георгиев"
message = MIMEText(body)
message["From"] = email_address
message["To"] = to_email
message["Subject"] = "Python Email"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_address, email_password)
    server.send_message(message)

print(" Email sent successfully.")