'''
Created on 12.5.2015

@author: e1201757
'''
month = None
months = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':30, 'Sep':31, 'Oct':30, 'Nov':31, 'Dec':30}
for month in months:
    if months.get(month) == 30:
        print (month)
