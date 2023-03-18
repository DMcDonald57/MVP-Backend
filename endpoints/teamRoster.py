from app import app
from flask import request, make_response, jsonify
from dbhelpers import run_statement

# endpoints to list rosters and have coach make changes

@app.get('/api/roster')
def team_roster():
    team_id = request.args.get('team_id')
    result = run_statement('CALL list_players (?)', [team_id])
    keys = ["first_name", "last_name", "position_played"]
    response = []
    if (type(result) == list):
        for first_name in result:
            response.append(dict(zip(keys,first_name)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result),500)
    
@app.get('/api/rosterupdate')
def teamFullroster():
    team_id = request.json.get('team_id')
    result = run_statement('CALL fullPlayerList (?)', [team_id])
    keys = ["first_name", "last_name", "phone_num", "email","position_played"]
    response = []
    if (type(result) == list):
        for first_name in result:
            response.append(dict(zip(keys,first_name)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result),500)
    