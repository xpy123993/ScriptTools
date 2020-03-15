"""
Calculate how many days spent each year based on travel history.

Basic usage:

    # Under the assumption that there is no overlapping intervals.
    travel_his = [('2017-06-26', '2018-09-19'),
                  ('2018-06-16', '2019-12-29'),
                  ('2020-06-06', '2020-09-19')]
    print(calculate_days_per_year(travel_his))
"""
from datetime import date
from collections import defaultdict


def calculate_days(start_date, end_date):
    val = (end_date - start_date).days
    if val < 0:
        # Raising error if there is a potential decrease
        # on the total spending days
        raise Exception(
            "start_date(%s) > end_date(%s)" % (start_date, end_date))
    return val


def begin_year_days(end_date):
    """Calculate days between (first day in that year, end_date)."""
    start_date = date.fromisoformat('%04d-01-01' % end_date.year)
    return calculate_days(start_date, end_date)


def end_year_days(start_date):
    """Calculate days between (start_date, last day in that year)."""
    end_date = date.fromisoformat('%04d-12-31' % start_date.year)
    return calculate_days(start_date, end_date)


def update_internal(start_date, end_date, update_dict):
    """Calculate how many days between `start_date` and `end_date`
    the result will be writen to `update_dict{year, days_in_that_year}`."""
    if start_date.year == end_date.year:
        update_dict[start_date.year] += calculate_days(start_date, end_date)
    else:
        update_dict[start_date.year] += end_year_days(start_date)
        update_dict[end_date.year] += begin_year_days(end_date)


def calculate_days_per_year(travel_history, date_extractor=date.fromisoformat):
    """Calculate how many days in each year based on travel history."""
    update_dict = defaultdict(int)
    for entry_date, leave_date in travel_history:
        update_internal(
            start_date=date_extractor(entry_date),
            end_date=date_extractor(leave_date),
            update_dict=update_dict)
    return update_dict


if __name__ == '__main__':
    travel_his = [('2017-06-26', '2018-01-19'),
                  ('2018-06-16', '2019-12-29'),
                  ('2020-06-06', '2020-09-19')]
    print(calculate_days_per_year(travel_his))
