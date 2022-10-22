from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    job_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    assert "title" in job_list[0]
    assert "salary" in job_list[0]
    assert "type" in job_list[0]
