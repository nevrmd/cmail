import configparser
import smtplib
from rich import print
from email.mime.text import MIMEText

try:
    # taking information from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

    sender_email = config["Sender"]["email"]
    sender_password = config["Sender"]["password"]
    print(
        f"Your [bold yellow]email[/bold yellow]: [bold green]{sender_email}[/bold green];\nYour [bold yellow]password[/bold yellow]: [bold green]{sender_password}[/bold green].\n")

    # taking other information
    to = input("Resiever's email (example@gmail.com): ")
    text = input("Text: ")

    # connect via a secure connection
    print("\n[bold cyan]Trying to connect via a secure connection...", end=" ")

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()

    print("[bold green]success!\n")

    # sending the email message
    print("[bold cyan]Trying to send an email...", end=" ")

    smtpObj.login(sender_email, sender_password)

    smtpObj.sendmail(sender_email, to, text)

    print("[bold green]success!")

# errors
except smtplib.SMTPAuthenticationError:
    print("[bold red]wrong email or password!")

except smtplib.SMTPRecipientsRefused:
    print("[bold red]invalid resiever's email")

except UnicodeError:
    msg = MIMEText(text, 'plain', 'utf-8')
    smtpObj.sendmail(sender_email, to, msg.as_string())
    print("[bold green]success!\n")

except:
    print(f"[bold red]some error occured\n")