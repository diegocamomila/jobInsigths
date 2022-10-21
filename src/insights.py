from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    jobs_types = set()
    for job in all_jobs:
        jobs_types.add(job["job_type"])
    return list(jobs_types)


if __name__ == "__main__":
    print(get_unique_job_types("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    all_jobs = read(path)
    industries = set()
    for job in all_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


if __name__ == "__main__":
    print(get_unique_industries("src/jobs.csv"))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    all_jobs = read(path)
    max_salaries = [
        int(job["max_salary"], 10)
        for job in all_jobs
        if job["max_salary"].isnumeric()
    ]
    return max(max_salaries)


if __name__ == "__main__":
    print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    all_jobs = read(path)
    min_salaries = [
        int(job["min_salary"], 10)
        for job in all_jobs
        if job["min_salary"].isnumeric()
    ]
    return min(min_salaries)


if __name__ == "__main__":
    print(get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
