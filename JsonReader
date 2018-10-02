import urllib.request, json


def getJson(request_url):
    url = str(request_url)
    req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    r = urllib.request.urlopen(req).read()
    json_data = json.loads(r.decode('utf-8'))

    return json_data

