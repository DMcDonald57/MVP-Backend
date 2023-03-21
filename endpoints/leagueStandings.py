from app import app
from flask import request, make_response, jsonify
from dbhelpers import run_statement


@app.get('/api/standings')
def league_standings():
    result = run_statement('CALL league_standings')
    keys = ["Team", "Win", "Loss"]
    response = []
    if (type(result) == list):
        for Team in result:
            response.append(dict(zip(keys,Team)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result),500)