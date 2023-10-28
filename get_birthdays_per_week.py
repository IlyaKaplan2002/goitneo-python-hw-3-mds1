import datetime
import collections
import calendar


def getWeekdaySortKey(key):
    return key[1]


def get_birthdays_per_week(users):
    today = datetime.datetime.today().date()

    res = collections.defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if birthday_this_year.weekday() == 5:
            birthday_this_year = birthday_this_year.replace(day=birthday.day + 2)

        if birthday_this_year.weekday() == 6:
            birthday_this_year = birthday_this_year.replace(day=birthday.day + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            res[
                (
                    calendar.day_name[birthday_this_year.weekday()],
                    birthday_this_year.weekday(),
                )
            ].append(name)

    keys = list(res.keys())
    keys.sort(key=getWeekdaySortKey)

    if len(keys):
        for key in keys:
            print(f"{key[0]}: {', '.join(res[key])}")
    else:
        print("There won't be birthdays on the next week")

    return res
