'''
Created on Nov 19, 2015

@author: arebrov
'''
import requests
from lxml import html,etree

URL = 'https://dprc.gov.ua/show.php?transport_type=2&src=22204001&dst=22218000&dt=2015-12-30&ret_dt=2001-01-01&ps=ec_privat'
#  URL = ''http://jsonplaceholder.typicode.com/users''

def send_get():
    response = requests.get(URL)
    if response.status_code == 200:
        print response.headers
        for jsonObject in response.json():
            # work with json as a dictionary
            print jsonObject['id']
            print jsonObject

def send_get_plain():
    response = requests.get(URL)
    if response.status_code == 200:
        #print response.headers
        #print response.content
        html_tree = html.fromstring(response.content)
        print html_tree
        expr = "//*[@class=$name]"
        trains = html_tree.xpath(expr,name="train_row")
        for train in trains:
            for el in train.iter():
                print el.text


send_get_plain()
