# src/webapp.py

from flask import Flask, render_template, request
from password_strength import evaluate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    password = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        result = evaluate_password(password)
    return render_template('index.html', result=result, password=password)

if __name__ == '__main__':
    app.run(debug=True)
