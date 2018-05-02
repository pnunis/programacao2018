import json
import requests

api_auth = 'X-CSRFToken: KhEeFMmRYdtfKKWmgSZH3RSZWp1YWwrcPH7BY7FNChzdMuAp3KIomKBjVornE9eQ'
#api_auth = 'KhEeFMmRYdtfKKWmgSZH3RSZWp1YWwrcPH7BY7FNChzdMuAp3KIomKBjVornE9eQ' #'MjAxNDIwMTQwNTA0NTY6UGF1bDE5MDU='
api_url_base = 'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic {0}'.format( api_auth)}

def get_account_info():
    response = requests.get(api_url_base, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

print (get_account_info())
