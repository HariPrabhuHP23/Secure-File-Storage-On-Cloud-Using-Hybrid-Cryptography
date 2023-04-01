from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__)

tot_users = {'users': {}}

print("inital ",tot_users)
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


@app.route('/receive', methods=['POST'])
def receivers():
    rece = request.form.getlist('file[]')
    print("receivers", rece)
    return rece


###Sending the existing user to dropdown #####
@app.route('/encrypt_users', methods=['GET'])
def jsondata():
    existing_users = {'user': ['Hari', "Krishnan", 'harish', 'prabhu']}
    return jsonify(existing_users)


### Login form authentication #####
@app.route("/login_form", methods=["GET", "POST"])
def login():
    with open("user.json", 'r') as data:
        users = json.load(data)
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for i in users:
            if i['username'] == username and i['repass'] == password:
                return render_template("choice.html", error=error)
        else:
            error = "Invalid username or password. Please try again."
            return error


#### sign in form registration ####
@app.route("/sign_form", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        with open("user.json", 'r') as data:
           users = json.load(data)

        username = request.form['username']
        name = request.form['name']
        mailid = request.form['mailid']
        newpass = request.form['newpass']
        repass = request.form['repass']
        if newpass != repass:
            return "Password not same", 404

        user = {'username': username, 'name': name, 'mailid': mailid, 'newpass': newpass, 'repass': repass}
        if any(user['mailid'] == mailid for user in users):
            return 'User already exists', 404
        else:
            users.append(user)
    with open('user.json', 'w') as f:
        json.dump(users, f)


    return render_template('main.html')


### Sending receivers and getting inputs from the webpage  decryption ####
@app.route('/decrypt_json', methods=['POST', 'GET'])
def receiverroute():
    if request.method == 'GET':
        receivers = {'files': ["1.pdf", "Harish.pdf", "3Prabhu.pdf"]}
        return jsonify(receivers)
    else:
        print("function ula vantan")
        image = request.files['file-upload']
        file_recv = request.form['dropdown_receiver']
        basepath = os.path.dirname(__file__)
        imagepath = os.path.join(basepath, 'Download/images', image.filename)
        image.save(imagepath)
        print(file_recv)
        print(image)
        return '<h1> File Downloading ........ </h1>'


### getting inputs from  encryption page ####
@app.route('/upload1', methods=['POST', 'GET'])
def upload1():
    if request.method == 'POST':
        print("--------------post________________")
        rece = request.form.getlist('file[]')
        print("List of receivers ---", rece)


        file = request.files['file--upload']
        image = request.files['img--upload']
        key = request.form['key']

        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads/files', file.filename)
        imagepath = os.path.join(basepath, 'uploads/images', image.filename)
        file.save(filepath)
        image.save(imagepath)

        print("________________________________________")
        print(" file path ---", filepath)
        print("________________________________________")
        print(" Image path ----", imagepath)


        print("Entered Key ---", key)
        text = "success"
    return text


if __name__ == '__main__':
    app.run()
