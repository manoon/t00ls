import requests
import json
import time
url = 'http://ezfm.china-plus.net/index.php?m=index&a=cat_list&cid=224'

r = requests.get(url)
content = r.text
decode_json = json.loads(content)

f = open('resfr0mAPI.txt','w')
for item in decode_json['data']:
        print item['id'] + " " + item['title'] + " " + item['url']
        #print >>f, item['url']+item['id']+item['title']
