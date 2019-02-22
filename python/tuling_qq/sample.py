import json
import requests
#import urllib
#import urllib

KEY = '45e71746ab2a46469da4ed6bc20dfe3b'
url = 'http://www.tuling123.com/openapi/api'



def get(text):
    req_info = u'{}'.format(text, ).encode('utf-8')
    query = {'key': KEY, 'info': req_info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
    r = requests.get(url, params=query, headers=headers)
    res = r.text
    print(json.loads(res).get('text').replace('<br>', '\n'))

if __name__=="__main__":
    text='讲个笑话'
    get(text)



