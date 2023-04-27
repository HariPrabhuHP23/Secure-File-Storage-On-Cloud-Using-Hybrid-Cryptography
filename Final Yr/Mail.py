from email.message import EmailMessage
import ssl
import smtplib
import os
import base64
from PIL import Image

def mail(img,options):
    path = 'C:/Users/harik/Secure-File-Storage-On-Cloud-Using-Hybrid-Cryptography/Final Yr/uploads/images/steganographed_img'


    file_data=os.path.join(path,img)




    sender="0101@gmail.com"
    send_password="dummy"

    #eamil_rec="harikrish0122001@gmail.com"
    eamil_rec=options

    sub="From secure Storage"

    em=EmailMessage()
    em['From']=sender
    em['To']=eamil_rec
    em['Subject']=sub
    em.set_content(" Your're encrypted image")

    with open(file_data,'rb') as f:
        img_data=f.read()
    em.add_attachment(img_data,maintype="image",subtype="png",filename=img)



    context=ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,send_password)
        smtp.sendmail(sender,eamil_rec,em.as_string())
        print("successfully Sent")

