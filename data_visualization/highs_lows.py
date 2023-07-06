import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	print(highs)


#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
#绘画最高气温曲线
plt.plot(dates, highs, c='red')
#绘画最低气温曲线
plt.plot(dates, lows, c='blue')
#给图标区域着色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形的格式
plt.title('Daily high temperatures, July 2014', fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
