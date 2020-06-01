from datetime import date, time, datetime, timedelta

def working_with_datetime():
    current_date = datetime.now()

    current_date_str = current_date.strftime('%d/%m/%y, %H:%M')
    print(current_date_str)

    weekdays = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom")
    print(weekdays[current_date.weekday()])

    made_up_date = datetime(2030, 5, 4, 15, 14, 15)
    print(made_up_date)

    string_date = '01/01/2001 15:14:15'
    converted_date = datetime.strptime(string_date, '%d/%m/%Y %H:%M:%S')
    print(converted_date)

    new_date = converted_date - timedelta(days=365)
    print(new_date)

def working_with_date():
    current_date = date.today()
    current_date_str = current_date.strftime('%A %B %C')
    print(current_date_str)

def working_with_time():
    time_a = time(hour=3, minute=14, second=15)
    print(time_a.strftime('%H:%M:%S'))

if __name__ == '__main__':
    working_with_date()
    working_with_time()
    working_with_datetime()