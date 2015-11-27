'''
Created on Nov 19, 2015

@author: arebrov
'''
import requests
import io
from lxml import html

URL = 'https://dprc.gov.ua/show.php?transport_type=2&src=22204001&dst=22218000&dt=2015-12-30&ret_dt=2001-01-01&ps=ec_privat'
#  URL = ''http://jsonplaceholder.typicode.com/users''
FILENAME = "c:/temp.html"


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
        expr = "//*[@class=$name]"
        trains = html_tree.xpath(expr, name="train_row")

        clear_file(FILENAME)
        for train in trains:
            info_rows = train.find_class("info_row")
            info_rows_result = map(lambda row: row.text, info_rows)
            to_file = ' '.join(info_rows_result).encode("utf-8")
            write_to_file(to_file)

            wagons = train.find_class("wagon_row")

            def function(wagon):
                price = wagon.find_class("price")
                print price
                if len(price) != 0:
                    return price[0].text + ' ' + wagon.find_class("seats_avail")[0].text
                else:
                    return ''

            wagon_result = map(function, wagons)
            to_file = ' '.join(wagon_result).encode("utf-8")

            write_to_file(to_file)


def clear_file(filename):
    file_to_write = open(filename, "w")
    file_to_write.truncate(0)
    file_to_write.close()


def write_to_file(content):
    file_save_trains = open(FILENAME, "a+")
    file_save_trains.write("\n")
    file_save_trains.write(content)
    file_save_trains.close()

send_get_plain()
