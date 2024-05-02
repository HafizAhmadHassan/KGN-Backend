import os
import pandas as pd
import smtplib, subprocess,time
import sys


def my_send_email():
    content="Hello World"
    mail=smtplib.SMTP('email-smtp.eu-central-1.amazonaws.com', 587)
    mail.ehlo()
    mail.starttls()
    sender='noreply@codexrsu4.it'
    recipient='develop@kgn.it'
    mail.login('AKIATCMPCKJUU5YZP3VR','BNmNLMXdCkelGRlP0sZ5rHBXmdnFegLdqhmLaqZF2kpz')
    header='To:'+ recipient +'\n'+'From:' \
    +sender+'\n'+'subject:testmail\n'
    content=header+content
    mail.sendmail(sender, recipient, content)
    mail.close()

file_original = os.path.join("", "/kaggle/input/sample/book3.xlsm")
df1 = pd.read_excel(file_original,'Sheet'+ sys.argv[2])

print( "Machine Configured : ", sys.argv[1])
count=0
num_Sheet=1

while(1):
    # This will be only run for one machine
    try:
        file_new = os.path.join("", "/kaggle/input/sample/book3.xlsm")
        df2 = pd.read_excel(file_new,'Sheet'+ sys.argv[2])
    except PermissionError :
        time.sleep(1)
        file_new = os.path.join("", "/kaggle/input/sample/book3.xlsm")
        df2 = pd.read_excel(file_new,'Sheet'+ sys.argv[2])

    data_frame_same = df1.equals(df2)
    if data_frame_same == 1:
        # wait some files and check the files again
        #print("Its Same seceond :",count)
        if count == 0:
            #os.system(f"python3 csv_to_mysql2.py {sys.argv[1]} 1")
            print("yes")
            #subprocess.run(['python3', 'csv_to_mysql2.py',sys.argv[1],'1','Sheet'+ sys.argv[2]]) # 1 means for insertion
        #exec(open("csv_to_mysql2.py").read())
        count=1
        time.sleep(1)
        
    else:
        print("Yes Change")

        # problem is double
        #subprocess.run(['python3', 'csv_to_mysql2.py',sys.argv[1],'0','Sheet'+ sys.argv[2]]) # 1 means for insertion

        count=count+1
        my_send_email()
        print("Email sent")
        """
        Implementation of Storage of Alarms


        we need the following to store
        1. Alarm Name
        2. Category 
        3. Text_Message
        4. To Whom We will send (depend on alarm )
        5. In database we need to see list of alarm status (Y/N) 
        
        - Lucid chart  DB design
        - Lets First Check Model in Django
        -
        


        """


        time.sleep(1)
        df1=df2
        time.sleep(1)


        # original df1 = assign kr do updated 
        #df1=df2
        # d2 ko bhi updates
        # run csv_to_sql
        #