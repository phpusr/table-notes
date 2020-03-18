import datetime


def parse_date(date_str):
    if date_str == '':
        return None

    dates = list(reversed(date_str.strip().split('.')))
    year = int(dates[0])
    month = int(dates[1]) if len(dates) >= 2 else 1
    day = int(dates[2]) if len(dates) >= 3 else 1
    return datetime.date(year, month, day)
