import crocodoc, requests

def document(file, uuid, pdf=False, annotated=False, filter=None):
    #Build query string
    querystring = "uuid=%s&token=%s" % (uuid, crocodoc.api_token)
    if pdf:
        querystring += "&pdf=true"
    if annotated:
        querystring += "&annotated=true"
    if filter:
        querystring += "&filter=%s" % (filter,)

    #GET request
    url = crocodoc.base_url + "download/document?" + querystring
    r = requests.get(url)
    
    #Success?
    if r.status_code == 200:
        return file.write(r.content)
    
    #Error?
    if r.json and "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Download error", r)
    
    
def thumbnail(file, uuid, size=(100,100)):
    #Validate inputs
    if isinstance(size, basestring):
        raise crocodoc.InvalidParamError("'size' should be a tuple of two integers: (width, height)")
        
    #Build query string
    querystring = "uuid=%s&token=%s&size=%dx%d" % (uuid, crocodoc.api_token, size[0], size[1])

    #GET request
    url = crocodoc.base_url + "download/thumbnail?" + querystring
    r = requests.get(url)
    
    #Success?
    if r.status_code == 200:
        return file.write(r.content)
    
    #Error?
    if r.json and "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Download error", r)
    
    
def text(file, uuid):
    #GET request
    querystring = "uuid=%s&token=%s" % (uuid, crocodoc.api_token)
    url = crocodoc.base_url + "download/text?" + querystring
    r = requests.get(url)
    
    #Success?
    if r.status_code == 200:
        return file.write(r.content)
    
    #Error?
    if r.json and "error" in r.json:
        raise crocodoc.APIError(r.json["error"], r)
    else:
        raise crocodoc.APIError("Download error", r)