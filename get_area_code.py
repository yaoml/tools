import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
    'Referer': 'http://www.weather.com.cn/weather1d/101010100.shtml'
    }
ret = requests.get('http://toy1.weather.com.cn/search?cityname=tahe', headers=headers)
ret.encoding = ret.apparent_encoding
area_json = json.loads(ret.text.split('(')[1].split(')')[0])
for i in area_json:
    print(i['ref'].split('~'))
