'''
Created on May 17, 2015

    A program which generates randomly a number of date and time values and displays them in Finnish language.

@author: Likai
'''
import random, datetime

MONTHS = ['', 'tammikuu', 'helmikuu', 'maaliskuu', 'huhtikuu', 'toukokuu', 'kesäkuu', 'heinäkuu', 'elokuu', 'syyskuu', 'lokakuu', 'marraskuu', 'joulukuu']
NUMBERS = ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän', 'kymmenen']
WEEKDAYS = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']

def numberInFinnish(num):
    length = len(str(num))
    if length < 5:
        literality = ''
        for i in range(length):
            digit = length - i
            if  digit == 4:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    literality += NUMBERS[int(str(num)[i])] + 'tuhat '
                else: literality += NUMBERS[int(str(num)[i])] + 'tuhatta '
            elif digit == 3:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    literality += NUMBERS[int(str(num)[i])] + 'yksisata '
                else: literality += NUMBERS[int(str(num)[i])] + 'sattaa '
            elif digit == 2:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    if str(num)[i + 1] == '0':
                        literality += 'kymmenen'
                    else: literality += NUMBERS[int(str(num)[i + 1])] + 'toista'
                else: literality += NUMBERS[int(str(num)[i])] + 'kymmentä'
            elif digit == 1:
                if num == int(str(num)[i]) or (length > 1 and str(num)[i - 1] != '1' and str(num)[i] != '0'):
                    literality += NUMBERS[int(str(num)[i])]
        return literality
    else: return 'This number is not supported!'

'''
SUFFIX1 = ['', 'kymmentä', 'sata', 'tuhat']
SUFFIX2 = ['', 'kymmentä', 'sataa', 'tuhatta']

def numberInFinnish(num):
    if num < 10000:
        literality = ''
        i = 0
        if num == 0: return NUMBERS[0]
        while num > 0:
            digit = int(num % 10)
            num /= 10
            if digit == 1:
                if i == 1:
                    if literality == '':
                        literality = 'kymmenen'
                    else: literality += 'toista'
                else: literality = NUMBERS[digit] + SUFFIX1[i] + literality
            elif digit > 1:
                literality = NUMBERS[digit] + SUFFIX2[i] + literality
            i += 1
    else:
        literality = 'This number is not supported!'
    return literality
'''

def getWeekday(year, month, day):
    return WEEKDAYS[int(datetime.datetime(year, month, day).strftime("%w"))]

def readDate(year, month, day):
    print('Tänään on ' + getWeekday(year, month, day) + ', ' + numberInFinnish(day) + ' ' + MONTHS[month] + 'ta, ' + numberInFinnish(year) + ' vuotta.' + ' (' + str(day) + '/' + str(month) + '/' + str(year) + ')')

def readTime(hour, minute):
    time = ''
    time += 'Kello on '
    if minute == 0:
        time += numberInFinnish(hour)
    elif minute in range(1, 30):
        time += numberInFinnish(minute) + ' yli ' + numberInFinnish(hour)
    elif minute == 30:
        time += 'puoli' + numberInFinnish(hour)
    elif minute in range(31, 60):
        time += numberInFinnish(60 - minute) + ' vaille ' + numberInFinnish(hour)
    time += '. (%d.%02d)' %(hour, minute)
#     if len(str(minute)) == 1:
#         time += ' (' + str(hour) + '.' + '0' + str(minute) + ')'
#     elif len(str(minute)) == 0:
#         time += ' (' + str(hour) + '.00' + ')'
#     else: time += ' (' + str(hour) + '.' + str(minute) + ')'
    print(time)
    
if __name__ == '__main__':
# Generate date:
    year = random.randrange(1000, 10000)
    month = random.randrange(1, 13)
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randrange(1, 32)
    elif month == 2:
        # if this year is a leap year
        if (not year % 4 and year % 100) or not year % 400:
            day = random.randrange(1, 29)
        else: day = random.randrange(1, 30)
        # Or it can be write in one line
        # day = random.randrange(1, 29) if (not year % 4 and year % 100) or not year % 400 else random.randrange(1, 30)
    else: day = random.randrange(1, 31)
    
    readDate(year, month, day)
    
    # Generate time:
    hour = random.randrange(0, 13)
    minute = random.randrange(0, 60)
    
    readTime(hour, minute)

'''
    # Or we generate date and time just by built-in function:
    timestamp = random.randint(0, 32510000000)
    DateTime = time.localtime(timestamp)
    
    year = DateTime.tm_year
    month = DateTime.tm_mon
    day = DateTime.tm_mday
    wday = DateTime.tm_wday
    hour = DateTime.tm_hour
    minute = DateTime.tm_minute

    readDate(year, month, day, wday)
    readTime(hour, minute)
 '''  
