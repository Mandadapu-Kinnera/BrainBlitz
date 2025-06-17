from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

valid_username = 'admin'
valid_password = 'password123'

@app.route('/')
def index():
    return render_template('index.html', error_display='none', error_message='')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == valid_username and password == valid_password:
        return redirect(url_for('welcome'))
    else:
        error_message = "Invalid username or password!"
        return render_template('index.html', error_display='block', error_message=error_message)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/brainblitz')
def brainblitz():
    return render_template('brainblitz.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/clickme')
def clickme():
    return render_template('clickme.html')

@app.route('/speakai')
def speakai():
    return render_template('speakai.html')

@app.route('/live')
def live():
    return render_template('live.html')

if __name__ == '__main__':
    app.run(debug=True)



