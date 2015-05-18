'''
Created on May 17, 2015

    A program which generates randomly a number of date and time values and displays them in Finnish language.

@author: Likai
'''
import random, datetime

MONTHS = {1:'tammikuu', 2:'helmikuu', 3:'maaliskuu', 4:'huhtikuu', 5:'toukokuu', 6:'kesäkuu', 7:'heinäkuu', 8:'elokuu', 9:'syyskuu', 10:'lokakuu', 11:'marraskuu', 12:'joulukuu'}
NUMBERS = {0: 'nolla', 1 : 'yksi', 2 : 'kaksi', 3 : 'kolme', 4 : 'neljä', 5 : 'viisi', 6 : 'kuusi', 7 : 'seitsemän', 8 : 'kahdeksan', 9 : 'yhdeksän', 10: 'kymmenen'}
WEEKDAYS = {0:'sunnuntai', 1:'maanantai', 2:'tiistai', 3:'keskiviikko', 4:'torstai', 5:'perjantai', 6:'lauantai'}
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
    time += '.'
    if len(str(minute)) == 1:
        time += ' (' + str(hour) + '.' + '0' + str(minute) + ')'
    elif len(str(minute)) == 0:
        time += ' (' + str(hour) + '.00' + ')'
    else: time += ' (' + str(hour) + '.' + str(minute) + ')'
    print(time)
   

# Generate date:
year = random.randrange(1000, 9999)
month = random.randrange(1, 13)
if month in (1, 3, 5, 7, 8, 10, 12):
    day = random.randrange(1, 31)
elif month == 2:
    # if this year is a leap year
    if (not year % 4 and year % 100) or not year % 400:
        day = random.randrange(1, 28)
    else: day = random.randrange(1, 29)
else: day = random.randrange(1, 30)

readDate(year, month, day)

# Generate time:
hour = random.randrange(0, 13)
minute = random.randrange(0, 60)

readTime(hour, minute)
