import smtplib

content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='ahmadhassan061@gmail.com'
recipient='f.sella@kgn.it'
mail.login('ahmadhassan061@gmail.com','jtjrwpaxovfqsgxv')
header='To:'+ recipient +'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()