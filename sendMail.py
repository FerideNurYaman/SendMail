from smtplib import SMTP

#SMPT simple mail transfer protocol tcp/ip protocol
try:
    #Mail Mesaj Bilgisi
    subcjet = "Test"
    message = "Bu bir test mesajıdır."
    content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri Örnek
    myMailAdress = "eposta@gmail.com"
    password = "şifre"

    # Gönderilecek Bilgisi Örnek
    sendTo = "hedef@gmail.com"

    mail = SMTP ("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress,sendTo, content.encode("utf-8"))
    print("mail gönderme işlemi başarılı")
except Exception as e:
    print("hata oluştu \n {0}".format(e))