import json

from flask import Flask, request
from flata import Flata, Query, where
from flata.storages import JSONStorage
db_init = Flata('db.json', storage=JSONStorage)
db_init.table('config', id_field = 'id')
db = db_init.get('config')

app = Flask(__name__)

#/db/data
@app.route('/data', methods=['GET'])
def get_data():
    q = request.args.get('q')
    if q:
        try:
            return db.all()[0]["config"][q]
        except KeyError:
            pass 
    return db.all()[0]["config"]

 

@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    db.purge()
    db.insert({"config": data})
    return get_data()

# #/db/data
# @app.route('/data', methods=['DELETE'])
# def delete_data():
#     current_config = get_data()
    
#     q = request.args.get('q')
#     if not q:
#         return "Need to send query", 400
#     try:
#         del current_config[q]
#     except KeyError:
#         return "Error", 400
#     db.purge()
#     db.insert({"config": current_config})
#     return "Success"



if __name__ == '__main__':
    

    #print(db.all())
    #db.purge()
    #db.insert({"config": config})
    app.run(debug=True,host="0.0.0.0", port=5000)
    
