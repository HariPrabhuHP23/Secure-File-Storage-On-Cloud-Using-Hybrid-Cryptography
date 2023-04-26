from flask import Flask, request, render_template, jsonify, send_file

import os
import enc
from stegano import lsb
from stegano.lsb import generators
import Mail
import dec

app = Flask(__name__)


#####Home Page#######
@app.route('/')
def index():
    return render_template('main.html')


### Back To Choice#####
@app.route('/back2choice', methods=["POST", "GET"])
def back2choice():
    return render_template('choice.html')


###Encryption Page###
@app.route('/upload', methods=["GET", 'POST'])
def upload():
    return render_template("encrypt.html")


### BACK TO LOGIN PAGE###
@app.route('/log_out', methods=["POST", "GET"])
def logout():
    return render_template("main.html")


### DECRYPTION PAGE###
@app.route('/download', methods=["POST", "GET"])
def download():
    return render_template("decrypt.html")


### Login form authentication #####
@app.route("/login_form", methods=["GET", "POST"])
def login():
    flag = True
    if request.method == "POST":
        mailid = request.form["mailid"]  ## mail id
        password = request.form["password"]  ## password

        data = {'Mail_id':mailid,'Password':password}### Json data of login details
        if flag == True:  ## Function call
            return render_template("choice.html")

        else:
            error = "Invalid username or password. Please try again."
            return error


#### sign in form registration ####
@app.route("/sign_form", methods=["POST"])
def sign():
    flag = True
    if request.method == "POST":
        ### Getting the sign in details as {mail: gmail,name:hhh,pass:123}
        data = request.json #get json in data variable
        print(data)
        if flag == True:
            return render_template('main.html')
        else:
            return "Sign in Fail!!!"


### Sending files and getting inputs from the webpage  decryption ####
@app.route('/decrypt_json', methods=['POST', 'GET'])
def receiverroute():
    if request.method == 'GET':
        files = [{'name':'hk.pdf','id':1},{'name':"Harish.pdf",'id':2},{'name':"Prabhu.pdf",'id':3}]###need files with name and id
        receivers=[]
        for i in files:
            receivers.append(i['name'])
        return jsonify(receivers)
    else:
        print("function ula vantan")
        files = [{'name': 'hk.pdf', 'id': 1}, {'name': "Harish.pdf", 'id': 2}, {'name': "Prabhu.pdf", 'id': 3}]### need function call
        image = request.files['image-upload']
        file_recv = request.form['dropdown_receiver']

        basepath = os.path.dirname(__file__)
        imagepath = os.path.join(basepath, 'Download/images', image.filename)
        image.save(imagepath)

        file_data = lsb.reveal(imagepath, generators.eratosthenes())

        print("steganogrpahd",file_data)

        key=dec.main(file_data)
        print("key",key)

        for i in files:#### retreiving the id and sending the key and id in json
            if i['name']==file_recv:
                data={'key':key,'id':i['id']}
                print(data)
                #return data you can get the json file here



        return '<h1> File Downloading ........ </h1>'


@app.route('/upload1', methods=['GET'])
def upload21():
    if request.method == 'GET':
        ###Sending the existing user to dropdown #####
        existing_users = {'user': ['harikrish0122001@gmail.com', "harishrethinam@gmail.com", 'hariprabhu2323@gmail.com',
                                   'ok@gmail.com']}
        return jsonify(existing_users)


### getting inputs from  encryption page ####
@app.route('/upload1', methods=['POST'])
def upload1():
    if request.method == 'POST':
        options=request.form.getlist('options')
        file = request.files['file--upload']
        image = request.files['img--upload']
        key = request.form['key']
        print("options ---",options)

        ##encrypting the entered key by passing the key encryption module
        encrypted_key = enc.main(key)

        ## obtaining the basepath or directory
        basepath = os.path.dirname(__file__)
        # print(basepath)

        ## saving the file
        filepath = os.path.join(basepath, 'uploads/files', file.filename)
        file.save(filepath)

        # saving the image and steganography process
        imagepath = os.path.join(basepath, 'uploads/images', image.filename)
        image.save(imagepath)

        hide = lsb.hide(imagepath, encrypted_key, generators.eratosthenes())
        imagepath1 = os.path.join(basepath, 'uploads/images/steganographed_img', 'steganographed_' + image.filename) #renaming the file name as steganographed_file name in order to differntitate the normal image and steg image
        hide.save(imagepath1)

        ## setting path
        #path = 'C:/Users/harik/Secure-File-Storage-On-Cloud-Using-Hybrid-Cryptography/Final Yr/uploads/images/steganographed_img'
        path=os.path.join(basepath,'uploads/images/steganographed_img')
        for filename in os.listdir(path):
            if filename == ("steganographed_" + image.filename):
                # checking the file name
                Mail.mail(filename,options)
                break
        #data = {'key': key, 'receivers': options}
        #if flag==True:
            #return data
        text = "success"

        return text


if __name__ == '__main__':
    app.run()
