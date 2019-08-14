import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
    'Referer': 'http://www.weather.com.cn/weather1d/101010100.shtml'
    }

ret = requests.get('http://d1.weather.com.cn/weather_index/101050702.html?_=1565759136666', headers=headers)
ret.encoding = ret.apparent_encoding
weather_data = ret.text.split(';')
print(weather_data[2].split('=')[1] + weather_data[3])
weather_json = json.loads(weather_data[2].split('=')[1] + weather_data[3])
print(weather_json)
