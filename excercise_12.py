import math
import datetime
current_dt = datetime.datetime.now()
day = int(input())
month = int(input())
year = int(input())
dt = datetime.datetime(year, month, day)

sum_of_days = 0

if (current_dt.year < dt.year):
    for m in range(current_dt.month, 13):
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            sum_of_days = sum_of_days + 31
        else:
            if (m == 4 or m == 6 or m == 9 or m == 11):
                sum_of_days = sum_of_days + 30
            else:
                if ((current_dt.year % 4 == 0 and current_dt.year % 100 !=0) or (current_dt.year % 400 == 0)):
                    sum_of_days = sum_of_days + 29
                else:
                    sum_of_days = sum_of_days + 28
        if (m == current_dt.month):
            sum_of_days = sum_of_days - current_dt.day
    for y in range(current_dt.year + 1, dt.year):
        if ((y % 4 == 0 and y % 100 != 0)or(y % 400 ==0)):
            sum_of_days = sum_of_days + 366
        else:
            sum_of_days = sum_of_days + 365
    for m in range(1, dt.month + 1):
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            if (m == dt.month):
                sum_of_days = sum_of_days + dt.day
                month_days = 31
            else:
                sum_of_days = sum_of_days + 31
        else:
            if (m == 4 or m == 6 or m == 9 or m == 11):
                if (m == dt.month):
                    sum_of_days = sum_of_days + dt.day
                    month_days = 30
                else:
                    sum_of_days = sum_of_days + 30
            else:
                if ((dt.year % 4 == 0 and dt.year % 100 != 0)or(dt.year % 400 == 0)):
                    if (m == dt.month):
                        sum_of_days = sum_of_days + dt.day
                        month_days = 29
                    else:
                        sum_of_days = sum_of_days + 29
                else:
                    if (m == dt.month):
                        sum_of_days = sum_of_days + dt.day
                        month_days = 28
                    else:
                        sum_of_days = sum_of_days + 28
    hours = 24 - current_dt.hour - 1
    mins = 60 - current_dt.minute
    secs = mins * 60 - current_dt.second
    print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
    print('The days of the given month are', month_days)
    print(current_dt)
else:
    if (dt.year < current_dt.year):
        for m in range(dt.month, 13):
            if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if (m == dt.month):
                    sum_of_days = sum_of_days + (31 - dt.day + 1)
                    month_days = 31
                else:
                    sum_of_days = sum_of_days + 31
            else:
                if (m == 4 or m == 6 or m == 9 or m == 11):
                    if (m == dt.month):
                        sum_of_days = sum_of_days + (30 - dt.day + 1)
                        month_days = 30
                    else:
                        sum_of_days = sum_of_days + 30
                else:
                    if ((dt.year % 4 == 0 and dt.year % 100 != 0)or(dt.year % 400 == 0)):
                        if (m == dt.month):
                            sum_of_days = sum_of_days + (29 - dt.day + 1)
                            month_days = 29
                        else:
                            sum_of_days = sum_of_days + 29
                    else:
                        if (m == dt.month):
                            sum_of_days = sum_of_days + (28 - dt.day + 1)
                            month_days = 28
                        else:
                            sum_of_days = sum_of_days + 28
        for y in range(dt.year + 1, current_dt.year):
            if ((y % 4 == 0 and y % 100 != 0)or(y % 400 == 0)):
                sum_of_days = sum_of_days + 366
            else:
                sum_of_days = sum_of_days + 365
        for m in range(1, current_dt.month + 1):
            if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                if (m == current_dt.month):
                    sum_of_days = sum_of_days + current_dt.day
                else:
                    sum_of_days = sum_of_days + 31
            else:
                if (m == 4 or m == 6 or m == 9 or m == 11):
                    if (m == current_dt.month):
                        sum_of_days = sum_of_days + current_dt.day
                    else:
                        sum_of_days = sum_of_days + 30
                else:
                    if ((current_dt.year % 4 == 0 and current_dt.year % 100 != 0)or(current_dt.year % 400 == 0)):
                        if (m == current_dt.month):
                            sum_of_days = sum_of_days + current_dt.day
                        else:
                            sum_of_days = sum_of_days + 29
                    else:
                        if (m == dt.month):
                            sum_of_days = sum_of_days + current_dt.day
                        else:
                            sum_of_days = sum_of_days + 28
        hours = current_dt.hour
        mins = current_dt.minute
        secs = mins * 60 + current_dt.second
        print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
        print('The days of the given month are', month_days)
        print(current_dt)
    else:
        if (current_dt.month < dt.month):
            for m in range(current_dt.month, dt.month + 1):
                if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                    if (m == dt.month):
                        sum_of_days = sum_of_days + dt.day
                        month_days = 31
                    else:
                        if (m == current_dt.month):
                            sum_of_days = sum_of_days + (31 - current_dt.day)
                        else:
                            sum_of_days = sum_of_days + 31
                else:
                    if (m == 4 or m == 6 or m == 9 or m == 11):
                        if (m == dt.month):
                            sum_of_days = sum_of_days + dt.day
                            month_days = 30
                        else:
                            if (m == current_dt.month):
                                sum_of_days = sum_of_days + (30 - current_dt.day)
                            else:
                                sum_of_days = sum_of_days + 30
                    else: 
                        if ((current_dt.year % 4 == 0 and current_dt.year % 100 != 0)or(current_dt.year % 400 == 0)):
                            if (m == dt.month):
                                sum_of_days = sum_of_days + dt.day
                                month_days = 29
                            else:
                                if (m == current_dt.month):
                                    sum_of_days = sum_of_days + (29 - current_dt.day)
                                else:
                                    sum_of_days = sum_of_days + 29
                        else:
                            if (m == dt.month):
                                sum_of_days = sum_of_days + dt.day
                                month_days = 28
                            else:
                                if (m == current_dt.month):
                                    sum_of_days = sum_of_days + (28 - current_dt.day)
                                else:
                                    sum_of_days = sum_of_days + 28
            hours = 24 - current_dt.hour - 1
            mins = 60 - current_dt.minute
            secs = mins*60 - current_dt.second
            print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
            print('The days of the given month are', month_days)
            print(current_dt)
        else:
            if (current_dt.month > dt.month):
                for m in range(dt.month, current_dt.month + 1):
                    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                        if (m == dt.month):
                            sum_of_days = sum_of_days + (31 - dt.day + 1)
                            month_days = 31
                        else:
                            if (m == current_dt.month):
                                sum_of_days = sum_of_days + current_dt.day
                            else:
                                sum_of_days = sum_of_days + 31
                    else:
                        if (m == 4 or m == 6 or m == 9 or m == 11):
                            if (m == dt.month):
                                sum_of_days = sum_of_days + (30 - dt.day + 1)
                                month_days = 30
                            else:
                                if (m == current_dt.month):
                                    sum_of_days = sum_of_days + current_dt.day
                                else:
                                    sum_of_days = sum_of_days + 30
                        else:
                            if ((current_dt.year % 4 == 0 and current_dt.year % 100 != 0)or(current_dt.year % 400 == 0)):
                                if (m == dt.month):
                                    sum_of_days = sum_of_days + (29 - dt.day + 1)
                                    month_days = 29
                                else:
                                    if (m == current_dt.month):
                                        sum_of_days = sum_of_days + current_dt.day
                                    else:
                                        sum_of_days = sum_of_days + 29
                            else:
                                if (m == dt.month):
                                    sum_of_days = sum_of_days + (28 - dt.day + 1)
                                    month_days = 28
                                else:
                                    if (m == current_dt.month):
                                        sum_of_days = sum_of_days + current_dt.day
                                    else:
                                        sum_of_days = sum_of_days + 28
                hours = 24 - (24 - current_dt.hour)
                mins = current_dt.minute
                secs = mins * 60 + current_dt.second
                print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
                print('The days of the given month are', month_days)
                print(current_dt)
            else:
                if (current_dt.day < dt.day):
                    sum_of_days = dt.day - current_dt.day
                    if (dt.month == 1 or dt.month == 3 or dt.month == 5 or dt.month == 7 or dt.month == 8 or dt.month == 10 or dt.month == 12):
                        month_days = 31
                    else:
                        if (dt.month == 4 or dt.month == 6 or dt.month == 9 or dt.month == 11):
                            month_days = 30
                        else:
                            if ((current_dt.year % 4 == 0 and current_dt.year % 100 != 0) or(current_dt.year % 400 == 0)):
                                month_days = 29
                            else:
                                month_days = 28
                    hours = 24 - current_dt.hour - 1
                    mins = 60 - current_dt.minute
                    secs = mins * 60 - current_dt.second
                    print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
                else:
                    if (current_dt.day > dt.day):
                        sum_of_days = current_dt.day - dt.day + 1
                        hours = 24 - (24 - current_dt.hour)
                        mins = current_dt.minute
                        secs = mins * 60 + current_dt.second
                        print(sum_of_days - 1, 'd', '/', hours, 'h', '/', secs, 's')
                    else:
                        print('The date coincides with the current date and has expireddate: ')
                        hours = current_dt.hour
                        mins = current_dt.minute
                        secs = mins * 60 + current_dt.second
                        print(0, 'd', '/', hours, 'h', '/', secs, 's')
                    if (dt.month == 1 or dt.month == 3 or dt.month == 5 or dt.month == 7 or dt.month == 8 or dt.month == 10 or dt.month == 12):
                        month_days = 31
                    else:
                        if (dt.month == 4 or dt.month == 6 or dt.month == 9 or dt.month == 11):
                            month_days = 30
                        else:
                            if ((current_dt.year % 4 == 0 and current_dt.year % 100 != 0) or(current_dt.year % 400 == 0)):
                                month_days = 29
                            else:
                                month_days = 28
                print('The days of the given month are', month_days)
                print(current_dt)
