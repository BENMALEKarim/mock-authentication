import os 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Karim BENMALEK and CoP DevOps: New version From ' + os.environ.get('APP_NAME') + ' application in ' + os.environ.get('ENVIRONMENT') + ' environment. Current verions is ' + os.environ.get('VERSION') + ' !'
#app.run(host=os.environ.get("HOST"), port=os.environ.get("PORT"))
port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)