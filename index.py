from flask import Flask
app = Flask(__name__)

@app.route('/')
def innit():
    return 'Gonna make those js devs mad'

@app.route('/bruv')
def bruv():
    return 'oi bruv is cheesday innit'
