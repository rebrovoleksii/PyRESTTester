'''
Created on Nov 19, 2015

@author: arebrov
'''
import requests

def send_get():
    response = requests.get('https://api.github.com/events');
    if response.status_code==200:
        print response.json();  

send_get();
