from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import random 
# add the argparser to fully fuction the program...
import argparse
parser = argparse.ArgumentParser(description='Mail spoofer and bomber')
parser.add_argument("-f","--file",help='Enter the file path if you want')
parser.add_argument('-n',"--number",help="Enter the amout how may time you want to send the mail",default=1 )
args = parser.parse_args()
# note you need to import to the sib_api_v3_sdk to install this exeute the cmd pip install sib_api_v3_sdk or pip3 install sib_api_v3_sdk
 
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = "your api key here"

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
s_mail =input("\033[33;1m Enter the subject: ")
subject = s_mail
# now ask for the actual msg 
# check if file name is empty 
if args.file:
    print("file name present")
msg_mail = input("\033[31;1m Enter msg to send")
html_content = msg_mail
sender_name = input("\033[32;1m Enter the sender name: ")
sender_email = input("\033[32;1m Enter the sender email: ")
sender = {"name":sender_name,"email":sender_email}
target_name = input("\033[32;1m Enter the target name: ")
target_email = input("\033[31;1m Entet the target email: ")

to = [{"email":target_email,"name":target_name}]
cc = [{"email":"example2@example2.com","name":"pata nahi"}]
bcc = [{"name":"sala","email":"example@example.com"}]
reply_to = {"email":"donotreply@domain.com","name":""}
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":subject}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
