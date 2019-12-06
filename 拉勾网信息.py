import requests
import json
import time
pages = int(input("你想爬取拉勾网站关于python工作多少页的信息: "))
print("正在爬取中：.................\n")
headers = {
		'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		}
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
for x in range(1,pages+1):
	data = {
			'first': 'true',
			'pn': x,
			'kd': 'python',
			}
	time.sleep(1)
	# 获取sessions
	ses = requests.session() # 跨请求保持参数不变
	ses.headers.update(headers)
	ses.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')

	content = ses.post(url,data)
	result = content.json()
	msgs = result['content']['positionResult']['result']
	for msg in msgs:
		location= msg['businessZones']
		city = msg['city']
		busyname = msg['companyFullName']
		saray = msg['companyLabelList']
		education = msg['education']
		type1 = msg['firstType']
		position = msg['positionLables']
		saray = msg['salary']
		times = msg['workYear']
		print(busyname,city,type1,position,location,saray,education,times)
