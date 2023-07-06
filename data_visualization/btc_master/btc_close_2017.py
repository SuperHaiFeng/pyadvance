from __future__ import (absolute_import, division, print_function, unicode_literals)

import json
import requests

import pygal
import math

from itertools import groupby

def get_btc_json(self):
	json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

	req = requests.get(json_url)

	#将数据写入文件
	with open('btc_close_2017.json','w') as f:
		f.write(req.text)

	json = req.json()

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
		# print(date, month, week, weekday, close)

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


def draw_line(x_data, y_data, title, y_legend):
	xy_map = []
	
	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _ : _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x, sum(y_list) / len(y_list)])

	# print(xy_map)
	# *为解包操作符，[*zip(*xy_map)]是将xy_map的子列表按照索引配对形成一个新列表
	x_unique, y_mean = [*zip(*xy_map)]

	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title + '.svg')
	return line_chart


#收盘价月日均值图
idx_month = dates.index('2017-12-12')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值', '月日均值')

#收盘价周日均值
ids_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:ids_week], closes[1:ids_week], '收盘价周日均值', '周日均值')

#收盘价星期均值
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], '收盘价星期均值', '星期均值')
line_chart_weekday.x_labels = wd
line_chart_weekday.render_to_file('收盘价星期均值.svg')


#将收盘价合并成仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf-8') as html_file:
	html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
	files = ['Closing price graph.svg', '收盘价对数变换折线图.svg', '收盘价月日均值.svg',
            '收盘价周日均值.svg', '收盘价星期均值.svg']
	for svg in files:
		html_file.write('<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
	html_file.write('</body></html>')



