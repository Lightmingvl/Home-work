import smtplib

fromaddr = '@gmail.com'
toaddrs  = '@gmail.com'
msg = 'Hello Kitty!'
gusername = 'user_@gmail.com'
gpassword = '02002020202'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(gusername,gpassword)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
