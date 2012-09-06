import crocodoc, requests

def create(uuid, **kwargs):
    #Validate session parameters
    data = { "uuid": uuid, "token": crocodoc.api_token } 
    boolean_parameters = ("editable", "admin", "downloadable", "copyprotected", "demo")  
    for key in list(kwargs.iterkeys()):
        if key in boolean_parameters:
            data[key] = "true" if bool(kwargs[key]) else "false"
            del kwargs[key]
    
    #User?
    if "user" in kwargs:
        data["user"] = kwargs["user"]
        del kwargs["user"]
            
    #Filter?
    if "filter" in kwargs:
        data["filter"] = kwargs["filter"]
        del kwargs["filter"]
    
    #Left-over arguments?
    if not kwargs == {}:
        raise crocodoc.InvalidParamError("invalid parameters: " + ', '.join(kwargs.iterkeys()))
    
    #POST request
    r = requests.post(crocodoc.base_url + "session/create", data)
    
    #Success?
    if r.json and "session" in r.json:
        return r.json["session"]
    
    #Error?
    if not r.json:
        raise crocodoc.APIError("Invalid JSON response", r)
    elif "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Missing session in JSON response", r)