import smtplib

fromaddr = 'lightmingvl@gmail.com'
toaddrs  = 'rudyi1@ucu.edu.ua'
msg = 'Hello Kitty!'
gusername = 'lightmingvl@gmail.com'
gpassword = '02071971'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(gusername,gpassword)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()