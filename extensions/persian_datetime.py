import jdatetime
from django.utils import timezone

def persian_numbers(str_arg):
    numbers = {
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
    }
    for e_num,p_num in numbers.items():
        str_arg = str_arg.replace(e_num, p_num)
    return str_arg
    

def time_to_int(time):
    time_to_integer = []
    year = int(time.strftime("%Y"))
    month = int(time.strftime("%m"))
    date = int(time.strftime("%d"))
    hour = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    secondes= int(time.strftime("%S"))
    time_to_integer.append(year)
    time_to_integer.append(month)
    time_to_integer.append(date)
    time_to_integer.append(hour)
    time_to_integer.append(minutes)
    time_to_integer.append(secondes)
    return time_to_integer
    
def persian_calender_datetime(time):
    time = timezone.localtime(time)
    time_in_int = time_to_int(time)
    jdatetime.set_locale("fa_IR")
    jalili_datetime =  jdatetime.datetime.fromgregorian(day=time_in_int[2],month=time_in_int[1],year=time_in_int[0],hour =time_in_int[3],minute=time_in_int[4],second=time_in_int[5])
    fa_date = jalili_datetime.strftime("%a, %d %b %Y %H:%M:%S")
    return persian_numbers(fa_date)
