import os 
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Hello Karim BENMALEK and CoP DevOps: From ' + os.environ.get('APP_NAME') + ' application in ' + os.environ.get('ENVIRONMENT') + ' environment. Current verions is ' + os.environ.get('VERSION')

@app.route('/login')
def login():
    return ' Your token is: ' + os.environ.get('TOKEN') + '. You must secure the token !!!'

@app.route('/newFeature')
def feature():
    return ' New Feature with Himansu'


port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)