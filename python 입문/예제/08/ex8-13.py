from datetime import datetime

today = datetime.now()

print('년 : %s' % today.year)
print('월 : %s' % today.month)
print('일 : %s' % today.day)
print('시 : %s' % today.hour)
print('분 : %s' % today.minute)
print('초 : %s' % today.second)

print(today.strftime('%Y/%m/%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %p %I:%M'))