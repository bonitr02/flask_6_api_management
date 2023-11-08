from flask import Flask, request, jsonify
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return f'Please enter your last 3 blood glucose test results. '

@app.route('/bg', methods =['GET'])
def blood_glucose_average():
    
    bg1 = request.args.get('bg1', "Please enter BG1 value again")
    bg2 = request.args.get('bg2', "Please enter BG2 value again")
    bg3 = request.args.get('bg3', "Please enter BG3 value again")
    
    bg1_real = int(bg1)
    bg2_real = int(bg2)
    bg3_real = int(bg3)

    average_bg = ((bg1_real + bg2_real + bg3_real)/3)

    output = json.dumps({
        "Blood glucose value #1": bg1_real,
        "Blood glucose value #2" : bg2_real,
        "Blood glucose value #3" : bg3_real,
        "Your average blood glucose values are": average_bg})
    return output

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
        )


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooper