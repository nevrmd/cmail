import configparser
import smtplib
from rich import print
from email.mime.text import MIMEText


def main():
    while True:
        try:
            print("""
1 - Send [cyan]email[/cyan]
2 - Change [cyan]email service[/cyan]
                 """)
            choice = int(input(">>> "))
        except ValueError:
            print("[bold red]Please, type number.")
        else:
            if choice == 1:
                # taking information from config.ini
                config = configparser.ConfigParser()
                config.read("config.ini")
                sender_email = config["Sender"]["email"]
                sender_password = config["Sender"]["password"]
                sender_host = config["SMTP"]["host"]
                sender_port = config["SMTP"]["port"]
                # showing this information
                print("\n[bold cyan]Information from [yellow]config.ini[/yellow] was read!")
                print(f"Your [bold yellow]email[/bold yellow]: [bold green]{sender_email}[/bold green];")
                print(f"Your [bold yellow]password[/bold yellow]: [bold green]{sender_password}[/bold green].\n")

                # taking other information
                to = input("Resiever's email (example@gmail.com): ")
                text = input("Text: ")
                # connect via a secure connection
                print("\n[bold cyan]Trying to connect via a secure connection...", end=" ")

                smtpObj = smtplib.SMTP(sender_host, sender_port)
                smtpObj.starttls()

                print("[bold green]success!\n")

                # sending the email message
                try:
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

            elif choice == 2:
                print("1 - [cyan]Gmail[/cyan] (default)\n2 - [cyan]Mail.ru[/cyan]\n3 - [red]Back[/red]\n")
                while True:
                    try:
                        service = int(input(">>> "))
                    
                    except ValueError:
                        print("[bold red]Please, type number.")
                    else:
                        if service == 1:
                            host = "smtp.gmail.com"
                            port = "587"
                            all_ok = True
                        
                        elif service == 2:
                            host = "smtp.mail.ru"
                            port = "465"
                            all_ok = True
                        
                        elif service == 3:
                            print("[bold red]Aborting...")
                            break
                        
                        else:
                            print("[bold red]Type 1 or 2 only!")
                            all_ok = False
                        
                        if all_ok:
                            config = configparser.ConfigParser()
                            config.read('config.ini')

                            config['SMTP']['host'] = host
                            config['SMTP']['port'] = port

                            with open('config.ini', 'w') as configfile:
                                config.write(configfile)
                            print("[bold green]Success!")

            else:
                print("[bold red]Type 1, 2 or 3 only!")


if __name__ == "__main__":
    main()
