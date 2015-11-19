'''
Created on Nov 19, 2015

@author: arebrov
'''
import requests

def send_get():
    response = requests.get('http://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        print response.headers
        for jsonObject in response.json():
        #work with json as a dictionary
            print jsonObject['id']
            print jsonObject

send_get();
