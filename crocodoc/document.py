import crocodoc, requests

def upload(url=None, file=None):
    #Validate token
    if not crocodoc.api_token:
        raise crocodoc.InvalidParamError("Please set an API token.")
    
    #POST request
    data = { "token": crocodoc.api_token }
    files = {}
    if file:
        files["file"] = file 
    if url:
        data["url"] = url
    r = requests.post(crocodoc.base_url + "document/upload", data=data, files=files)
    
    #Success?
    if r.json and "uuid" in r.json:
        return r.json["uuid"]
    
    #Error?
    if not r.json:
        raise crocodoc.APIError("Invalid JSON response", r)
    elif "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Missing uuid in JSON response", r)

def status(uuids):
    #Single uuid?
    if isinstance(uuids, basestring):
        uuids = [uuids]
    
    #GET request
    querystring = "uuids=%s&token=%s" % (",".join(uuids), crocodoc.api_token)
    url = crocodoc.base_url + "document/status?" + querystring
    r = requests.get(url)
    
    #Got status?
    if r.json:
        return r.json
    #Error?
    else:
        raise crocodoc.APIError("Invalid JSON response", r)

def delete(uuid):
    #POST request
    data = { "uuid": uuid, "token": crocodoc.api_token }
    url = crocodoc.base_url + "document/delete"
    r = requests.post(url, data)

    #Success?
    if r.json and r.json == True:
        return

    #Error?
    if not r.json:
        raise crocodoc.APIError("Invalid JSON response", r)
    elif "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Unexpected JSON response", r)