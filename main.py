import json

from flask import Flask, request

app = Flask(__name__)

#db/data

@app.route('/data', methods=['GET', 'POST'])
def password():
    if request.method == 'GET':        
        return {}
    elif request.method == 'POST':
        return {}


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
    
