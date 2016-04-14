import smtplib
fromaddr = 'lightmingvl@gmail.com'
toaddrs  = 'rudyi1@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know! Nevermind, rejoice!'
username = 'lightmingvl@gmail.com'
password = '02071971'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(gusername,gpassword)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()