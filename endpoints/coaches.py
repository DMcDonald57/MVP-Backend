from app import app
from flask import request, make_response, jsonify
from dbhelpers import run_statement
import json
import uuid

#endpoints for coaches go here

@app.post('/api/coaches')
def coach_login():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    result = run_statement("CALL verify_coach (?)", [email])
    coach_id=result[0][0]
    storedpassword=result[0][1]
    if storedpassword != password:
        return make_response(jsonify("Password does not match"),401)
    result = run_statement('CALL coach_login (?,?)', [coach_id, token])
    if (type(result) == list):
        response = {
            "coachId" : result[0][0],
            "token" : result[0][1]
        }
        return make_response(jsonify(response), 201)
    else:
        return make_response(jsonify(result), 500)