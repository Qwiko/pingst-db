import json

from flask import Flask, request

from flata import Flata, Query, where

from flata.storages import JSONStorage

db_init = Flata('db.json', storage=JSONStorage)
db_init.table('config', id_field = 'id')
db = db_init.get('config')

#from flask_cors import CORS



# config = {
#     "ProPresenter7": {
#         "PRO7_HOST": "192.168.0.100",
#         "PRO7_PORT": "20563",
#         "PRO7_CONTROL_PASSWORD": "control",
#         "PRO7_TARGET_GROUPNAME": "Powerpoint"
#     },
#     "Unifi": {
#         "username": "admin",
#         "password": "admin",
#         "baseurl": "https://192.168.0.128:8443",
#         "site": "default",
#         "verify_ssl": False
#     }
#   }

app = Flask(__name__)
#CORS(app)

#/db/data
@app.route('/data', methods=['GET', 'POST'])
def password():
    if request.method == 'GET':  
        return db.all()[0]["config"]
        #return config
    elif request.method == 'POST':
        data = request.json["data"]
        if not data:
            print("No value")
            return db.all()[0]["config"]
        db.purge()
        db.insert({"config": data})
        return db.all()[0]["config"]


if __name__ == '__main__':
    

    #print(db.all())
    #db.purge()
    #db.insert({"config": config})
    app.run(debug=True,host="0.0.0.0", port=5000)
    
