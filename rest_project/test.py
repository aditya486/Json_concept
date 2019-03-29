import requests
import json
BASE_URL= 'http://127.0.0.1:8000/'
ENDPOINT = 'list/'
def get_resource(id):
    resp=request.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
def get_all():
    resp = requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())

# get_all()
def create_resource():
    new_emp={
    'eno':700,
    'ename':'katrina',
    'esal':7000,
    'eaddr':'Mumbai',
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resource()
