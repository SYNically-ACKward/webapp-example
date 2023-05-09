from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

users = {'username1': 'password1', 'username2': 'password2'}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            error = 'Invalid username'
        elif users[username] != password:
            error = 'Invalid password'
        else:
            return redirect(url_for('success'))
    return render_template('login.html', error=error)

@app.route('/success')
def success():
    return 'You are now logged in!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
