import datetime

import selenide.cneducard as card
from selenide.dataconfig import BROWSER

# print(BROWSER)
# browser = input('输入浏览器：')
# name = input('输入名称：')
card.config('chrome', '首页', 'report', 1)
# date = '2012-8-9'
# try:
#     date = datetime.datetime.strptime(date, '%Y-%m-%d')
# except ValueError:
#     print('日期格式错误')
# date_today = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d')
# days = str(date - date_today).replace('0:00:00', '0')
# days2 = days.replace('days, 0', '')
# i_offset = int(days2)
# print(days2)
