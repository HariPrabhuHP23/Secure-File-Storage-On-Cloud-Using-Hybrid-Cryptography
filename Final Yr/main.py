from flask import Flask, request, render_template, url_for, redirect
import json

app = Flask(__name__)

tot_users = []


@app.route('/')
def index():
    return render_template('main.html')


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


@app.route('/upload', methods=["POST", "GET"])
def upload():
    return render_template("encrypt.html")


@app.route('/log_out', methods=["POST", "GET"])
def logout():
    return render_template("main.html")


@app.route('/download', methods=["POST", "GET"])
def download():
    return render_template("decrypt.html")


@app.route('/filedata', methods=['POST'])
def myroute():
    file = request.form['file']
    print(file)
    return 'ok'


@app.route('/receiverdata', methods=['POST', 'GET'])
def receiverroute():
    receivers = request.get_json()
    print(receivers)
    '''
    receivers=(info['data'] if info['operation']=='reciver' else "None")
    img=(info['data'] if info['operation']=='imageupload' else "None")
    file = (info['data'] if info['operation'] == 'fileupload' else "None")
    print(f' {receivers} {img} {file}')
    '''
    return 'ok'

@app.route('/file_encrypt', methods=['POST', 'GET'])
def fileroute():
    file = request.get_json()
    print(file)
    return ' OK '




@app.route('/imagedata', methods=['POST', 'GET'])
def imgroute():
    img= request.get_json()
    print(img)
    return 'OK '





@app.route('/back2choice', methods=["POST", "GET"])
def back2choice():
    return render_template('choice.html')


if __name__ == '__main__':
    app.run()
