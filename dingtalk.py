import requests
import json
import urllib.parse
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=cdd3aa55dad484ee30f9a765cb3ff1a83c56b2c05f597eff654d25007abee0f3'
HEADERS = {"Content-Type": "application/json ;charset=utf-8 "}
main_content='1小时调度报错,请检查!现在时间是: '+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(main_content)

String_textMsg = {"msgtype": "text","text": {"content": main_content }}
String_textMsg = json.dumps(String_textMsg)
res = requests.post(url, data=String_textMsg, headers=HEADERS)
print(res.text)
