def login(request, database):
    print(request.body["login"])
    if database.check_auth(request.body["login"], request.body["password"]):
        return '{"success": "true"}'
    else:
        return '{"success": "false"}'
    
