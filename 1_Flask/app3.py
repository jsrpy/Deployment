from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('textbox.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    magic = request.form['magic']
    magic_transform = ''.join([random.choice(magic.upper()) for i in range(len(magic))])
    if text != '':
        return 'Here is your input: ' + processed_text
    else:
        return 'MAGICCC: ' + magic_transform