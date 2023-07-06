from __future__ import (absolute_import, division, print_function, unicode_literals)

import json
import requests

import pygal
import math

def get_btc_json(self):
	json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

	req = requests.get(json_url)

	#将数据写入文件
	with open('btc_close_2017.json','w') as f:
		f.write(req.text)

	json = req.json()
	print(json)

#读取数据
filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)

	for btc_dict in btc_data:
		date = btc_dict['date']
		month = int(btc_dict['month'])
		week = int(btc_dict['week'])
		weekday = btc_dict['weekday']
		close = int(float(btc_dict['close']))
		print(date, month, week, weekday, close)

"""绘制收盘价折线图"""
dates, months, weeks, weekdays, closes = [], [], [], [], []

for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	closes.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换(¥)'
line_chart.x_labels = dates
N = 30 #x轴每隔30天显示一次
line_chart.x_labels_major =dates[::N]
close_log = [math.log10(_) for _ in closes]
line_chart.add('log收盘价', close_log)
# line_chart.add('收盘价(¥)', closes)
line_chart.render_to_file('收盘价对数变换折线图.svg')


