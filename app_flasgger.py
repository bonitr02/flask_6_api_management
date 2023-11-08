from flask import Flask, request, jsonify
from flasgger import Swagger
import json

app = Flask(__name__)
Swagger(app)

@app.route('/bg', methods =['GET'])
def blood_glucose_average(): 
   
    """
    The endpoint returns the entered blood glucose value.
    ---
    parameters:
    - name: blood_glucose
    in: query
    description: Blood glucose value
    type: integer
    default: 0

    responses:
        200:
            description: Returns the blood glucose value.

    """

    blood_glucose = request.args.get('blood_glucose', 0)
    return f'Blood glucose value #1: {blood_glucose}'

if __name__ == '__main__':
    app.run(debug=True)
