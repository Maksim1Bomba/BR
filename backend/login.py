import json

def login(request, database):
    print(request.body["login"], request.body["password"])
    if request.body["login"]:# database.check_auth(request.body["login"], request.body["password"]):
        return json.load('{"success": "true"}')
    else:
        return json.load('{"success": "false"}')
    
