from typing import Dict

week_days = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday',
             4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}

START_DATE = (1900, 1, 1)  # Year, Month, Day
START_DAY = 2
TARGET_DAY = 'Sunday'


def year_months(n: int) -> Dict[int, int]:
    normal_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        return leap_year
    else:
        return normal_year


def days_diff(start_date: tuple, end_date: tuple) -> int:
    output = 0

    # Start date and end date sharing year or year and month
    if start_date[0] == end_date[0]:
        if start_date[1] == end_date[1]:
            return end_date[2] - start_date[2]
        else:
            y = year_months(start_date[0])
            output += y[start_date[1]] - start_date[2]
            for i in range(start_date[1] + 1, end_date[1]):
                output += y[i]
            output += end_date[2]
            return output

    # Counting remaining days of the start date year if end date year is larger
    y = year_months(start_date[0])
    output += y[start_date[1]] - start_date[2]
    for i in range(start_date[1] + 1, 13):
        output += y[i]

    # Counting the years in between start date year and end date year
    for i in range(start_date[0] + 1, end_date[0]):
        y = year_months(i)
        output += sum(y.values())

    # Counting the days in the end date year before the end date month
    for i in range(1, end_date[1]):
        y = year_months(end_date[0])
        output += y[i]

    # Counting the days in the month of end date
    output += end_date[2]

    return output


target = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        diff = days_diff(START_DATE, (i, j, 1))
        if week_days[(diff + START_DAY) % 7] == TARGET_DAY:
            target += 1

print(target)
