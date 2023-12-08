day_of_weeks = {
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday',
    8: 'Sunday'
}


def day_in_week(day_int):
    return day_of_weeks.get(day_int, 'Invalid day')
