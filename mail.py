import smtplib

m = open("maillist.txt", "r")
m2 = open("maillist.txt", "r")
m1 = m2.read()
mail_list = m.readlines()


def send_mail():
    user = "maanav.acharya@gmail.com"
    passw = "mynameejeff"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, passw)
    for i in mail_list:
        i = i.strip()
        msg = "\r\n".join([
            "From: maanav.acharya@gmail.com",
            "To: %s" % i,
            "Subject: Free Anti Virus",
            "",
            "Download Free Anti Virus Here - https://drive.google.com/drive/folders/1fo0gHfmkFdwyjSkgV34heiQehE-OOXxJ?usp=sharing"
        ])
        print(msg)
        server.sendmail(user, i, msg)
