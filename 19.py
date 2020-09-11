from euler import elapsed_time


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    return False


def days_in_year(year):
    return 366 if is_leap_year(year) else 365


def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 31


def doy_to_dom(doy, year):
    rot = 0
    for m in range(1,13):
        dim = days_in_month(m, year)
        rot += dim
        if rot >= doy:
            return doy - (rot - dim)
    raise ValueError("doy is to large")


@elapsed_time()
def solve():
    """How many sundays fell on the first of the month between jan 1st 1901 and dec 31 2000

    Things i know:
    - leap year = lambda year : year % 4 == 0
    """
    ans = 0
    doy = 6 # 1/6/1901 is the first sunday.
    year = 1901

    while year < 2001:
        if doy_to_dom(doy, year) == 1:
            ans += 1
        doy += 7
        if doy > days_in_year(year):
            doy = doy - days_in_year(year)
            year += 1

    return ans


if __name__ == "__main__":
    print("ans:", solve())
