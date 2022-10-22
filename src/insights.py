from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    jobs_types = set()
    for job in all_jobs:
        jobs_types.add(job["job_type"])
    return list(jobs_types)


# if __name__ == "__main__":
#     print(get_unique_job_types("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    job_filter = [job for job in jobs if (job["job_type"] == job_type)]
    # print(job_filter)
    return job_filter


def get_unique_industries(path):
    all_jobs = read(path)
    industries = set()
    for job in all_jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


# if __name__ == "__main__":
#     print(get_unique_industries("src/jobs.csv"))


def filter_by_industry(jobs, industry):
    job_filter = [job for job in jobs if job["industry"] == industry]
    # print(job_filter)
    return job_filter


def get_max_salary(path):
    all_jobs = read(path)
    max_salaries = [
        int(job["max_salary"], 10)
        for job in all_jobs
        if job["max_salary"].isnumeric()
    ]
    return max(max_salaries)


# if __name__ == "__main__":
#     print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    all_jobs = read(path)
    min_salaries = [
        int(job["min_salary"], 10)
        for job in all_jobs
        if job["min_salary"].isnumeric()
    ]
    return min(min_salaries)


# if __name__ == "__main__":
#     print(get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    if (
        "min_salary" in job
        and "max_salary" in job
        and type(job["min_salary"]) == int
        and type(job["max_salary"]) == int
        and type(salary) == int
        and job["min_salary"] < job["max_salary"]
    ):
        # print(job)
        return job["min_salary"] <= salary <= job["max_salary"]
    else:
        raise ValueError("chaves não informadas")


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            match = matches_salary_range(job, salary)
            if match:
                result.append(job)
        except ValueError:
            pass
    return result
