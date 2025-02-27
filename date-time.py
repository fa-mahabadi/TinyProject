from datetime import datetime
import jdatetime


date_time_1 = input("Enter first DateTime: ")
date_time_2 = input("Enter second DateTime: ")
date_time_1 = datetime.strptime(date_time_1, "%Y-%m-%d %H:%M:%S")
date_time_2 = datetime.strptime(date_time_2, "%Y-%m-%d %H:%M:%S")
timedelta = (date_time_1 - date_time_2).total_seconds()
print(f"diffrence between two time is {timedelta} seconds")


def convert_to_jalali(dt):
    return jdatetime.datetime.fromgregorian(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
    )


jalali_datetime_1 = convert_to_jalali(date_time_1)
jalali_datetime_2 = convert_to_jalali(date_time_2)
print(f"jalali first datetime is {str(jalali_datetime_1)} ")
print(f"jalali second datetime is {str(jalali_datetime_2)} ")



def count_leap_year(first_year,second_year):
    leap_year=0
    for i in range(second_year,first_year+1):
        is_leap_year = jdatetime.datetime(year=i, month=1, day=1).isleap()
        if is_leap_year:
            leap_year+=1
    print(f'count of leap year is: {leap_year}')

first_year=jalali_datetime_1.year
second_year=jalali_datetime_2.year
count_leap_year(first_year,second_year)

