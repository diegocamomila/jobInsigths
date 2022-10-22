from src.counter import count_ocurrences


def test_counter():
    count = count_ocurrences("src/jobs.csv", "developer")
    print(count)
    # return count
    assert count == 352
