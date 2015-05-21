p_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def interpret_western_sign(day, month):
    if month < 0 or month > 12 or day < 0 or day > 31:
        return

    # structure is:
    # (day_upper_bound, sign, day_lower_bound, sign)
    western_signs = {
        1: (20, "capricorn", 21, "aquarius"),
        2: (18, "aquarius", 19, "pisces"),
        3: (20, "pisces", 21, "aries"),
        4: (20, "aries", 21, "taurus"),
        5: (20, "taurus", 21, "gemini"),
        6: (20, "gemini", 21, "cancer"),
        7: (22, "cancer", 23, "leo"),
        8: (22, "leo", 23, "virgo"),
        9: (22, "virgo", 23, "libra"),
        10: (22, "libra", 23, "scorpio"),
        11: (21, "scorpio", 22, "sagittarius"),
        12: (21, "sagittarius", 22, "capricorn")
    }

    date_tuple = western_signs[month]
    if day <= date_tuple[0]:
        return date_tuple[1]
    elif day >= date_tuple[2]:
        return date_tuple[3]


def interpret_chinese_sign(year):
    chinese_signs = {
        1900: "rat",
        1901: "ox",
        1902: "tiger",
        1903: "rabbit",
        1904: "dragon",
        1905: "snake",
        1906: "horse",
        1907: "sheep",
        1908: "monkey",
        1909: "rooster",
        1910: "dog",
        1911: "pig"
    }

    for y in chinese_signs:
        if abs(y - year) % 12 == 0:
            return chinese_signs[y]


def interpret_both_signs(day, month, year):
    # do double check once here once in interpret_western_sign
    # because in case of wrong day or month input this function
    # will return partial result
    if month <= 0 or month > 12 or day <= 0 or day > 31:
        return

    # check if day is 29 02 if the year is leap
    if day == 29 and month == 2:
        if not leap_year(year):
            return

    western_sign = interpret_western_sign(day, month)
    chinese_sign = interpret_chinese_sign(year)

    return (western_sign, chinese_sign)
