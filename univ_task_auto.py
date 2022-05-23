import requests
import pandas as pd
import datetime
import re
from pprint import pprint
import json
day_of_week    = {'Mon': 0,'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
notion_api_key = 'secret_1NollZhmAlXJs5GnL5Twflda7dmTB4rGRFoWWMSeQOM'
database_id    = "751c089a0f914cf8b1cfcda6bda84895"
headers        = {'Authorization': f'Bearer {notion_api_key}',
                  'Content-Type' : 'application/json',
                  'Notion-Version': '2022-02-22'}


def get_request_url(end_point):
    return f'https://api.notion.com/v1/{end_point}'

def class_register(kamoku, youbi, kadai_due_day, kadai_due_time='23:59'):
    
    property_name  = {"title": [{"text": {"content": kamoku}}]}
    property_select = {"select": {"name": "weekly"}}
    property_youbi = {"date": {"start": (datetime.date.today()+datetime.timedelta(days=day_of_week[youbi]))}}
    if kadai_due_day == None:
        property_date = {"date": {"start": (datetime.date.today()+datetime.timedelta(days=0-datetime.date.today().weekday())+datetime.timedelta(days=21)).isoformat()+" "+kadai_due_time}}
    else:
        property_date = {"date": {"start": (datetime.date.today()+datetime.timedelta(days=0-datetime.date.today().weekday())+datetime.timedelta(days=kadai_due_day)).isoformat()+" "+kadai_due_time}}

    body = {
    "parent": {
    "database_id": database_id},
    "properties": {
        "task name": property_name,
        "due": property_date,
        "type": property_select,
        "date": property_youbi
        }
    }
    response = requests.request('POST', url=get_request_url('pages'), headers=headers, data=json.dumps(body))
    pprint(response.json())
    print('\n--------------------------------------------------------------------------------\n')

class_register('回路理論', 'Mon', 7, '09:00')
class_register('プログラミングA演習', 'Mon', 3, '13:00')
class_register('プログラミングA宿題', 'Mon', 7, '13:00')
class_register('Academic Reading', 'Mon', 7, '16:30')
class_register('社会心理学', 'Tue', 7, '09:00')
class_register('情報倫理', 'Tue', 3, '10:40')
class_register('理工学基礎実験', 'Tue', 7, '23:59')
class_register('before論理回路', 'Tue', 6, '23:59')
class_register('after論理回路', 'Tue', None)
class_register('Concept Building and Discussion', 'Wed', 7, '16:30')
    