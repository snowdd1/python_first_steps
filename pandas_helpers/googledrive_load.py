from io import StringIO
#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
def get_string_handle_from_google_drive_share(id):
    baseurl = 'https://drive.google.com'
    URL = baseurl + '/uc?export= ' + id
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    sr = response
    sr.encoding='utf-8'
    return StringIO(sr.text)
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None
    
