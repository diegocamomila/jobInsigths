from operator import itemgetter
from src.sorting import sort_by


mocks = [
    {"min_salary": 2500, "max_salary": 3000, "date_posted": "2022-09-12"},
    {"min_salary": 6000, "max_salary": 7000, "date_posted": "2021-08-22"},
]


def test_sort_by_criteria():
    sort_by(mocks, "max_salary")
    newlist = list(mocks)
    expected1 = sorted(newlist, key=itemgetter("max_salary"), reverse=True)
    assert expected1 == mocks
    sort_by(mocks, "min_salary")
    expected2 = sorted(newlist, key=itemgetter("min_salary"), reverse=False)
    assert expected2 == mocks
    sort_by(mocks, "date_posted")
    expected3 = sorted(newlist, key=itemgetter("date_posted"), reverse=True)
    assert expected3 == mocks
