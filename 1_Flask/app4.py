from flask import Flask, request, render_template, json
import string, csv, datetime
#from time import gmtime, strftime, localtime

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('textbox2.html')

def encrypt_lower(text,key):
    char2num = {k:i for i,k in enumerate(string.ascii_lowercase)}
    num2char = {k:i for k,i in enumerate(string.ascii_lowercase)}
    return "".join([ num2char[(char2num[c] + key) % 26 ] if c.isalpha() else c  for c in text])

def encrypt_upper(text,key):
    char2num = {k:i for i,k in enumerate(string.ascii_uppercase)}
    num2char = {k:i for k,i in enumerate(string.ascii_uppercase)}
    return "".join([ num2char[(char2num[c] + key) % 26 ] if c.isalpha() else c  for c in text])

def encrypt(text,key):
    return "".join([ encrypt_lower(char,key) if char.islower() else encrypt_upper(char,key) for char in text ])

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed = encrypt(text,3)
    print(request.form.get('name'))
    print(request.form.get('text'))
    z = request.form.get('name')
    x = request.form.get('text')
    #y = strftime("%Y-%m-%d %H:%M:%S", localtime())
    y = str(datetime.datetime.now()).split('.')[0]
    #with open('file.json', 'a') as f:
    #    json.dump({'str':x,'time':y}, f)
    with open('record.csv', 'a+') as f:
        f.write('\n')
        f.write(z+','+x+','+y)
    return processed

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
