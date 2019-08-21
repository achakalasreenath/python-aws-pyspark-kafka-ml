import datetime


def times():
    # using floating point values for microseconds generates an error
    t = datetime.time(1, 2, 3, 4)
    print(t)
    print("Hours:{}".format(t.hour))
    print("Minutes:".format(t.minute))
    print("seconds:".format(t.second))
    print("Microseconds".format(t.microsecond))
    print("Min:{}".format(t.min))
    print("Max:{}".format(t.max))
    print("Resolution".format(t.resolution))


def dates():
    today = datetime.date.today()
    print(today)
    print("Time:{}".format(today.ctime()))
    print("Day:{}".format(today.day))
    print("Month:{}".format(today.month))
    print("Year:{}".format(today.year))
    print("Timetuple:{}".format(today.timetuple()))
    print("Min:{}".format(today.min))
    print("Max:{}".format(today.max))
    print("Resolution:{}".format(today.resolution))

    day1 = datetime.date(2008, 6, 24)
    day2 = day1.replace(year=2019)
    print(day1)
    print(day2)

    #Time Delta
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    tommorrow = today + oneday

    # Date Arithmetic
    print("Yesterady :", yesterday)
    print("Tommorrow :", tommorrow)
    print(tommorrow - yesterday)
    print(yesterday - tommorrow)

    # comparing dates
    print(tommorrow > yesterday)
    print(yesterday > tommorrow)

def datetimes():
    t = datetime.time(1,2,3)
    today = datetime.date.today()
    todayt = datetime.datetime.combine(today,t)
    print(t,today,todayt)

    d = datetime.datetime.now()
    for attr in ['day','month','year','hour','minute','second','microsecond']:
        print("{} : {}".format(attr,getattr(d,attr)))

if __name__ == '__main__':
    print("---------Time---------")
    times()
    print("---------Date---------")
    dates()
    print("---------DateTime-----")
    datetimes()

