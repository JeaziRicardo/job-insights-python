from typing import Union, List, Dict
from src.insights.jobs import (read)


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    return max([
        int(job['max_salary'])
        for job in jobs_list
        if job['max_salary'].isdigit()
    ])


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    return min([
        int(job['min_salary'])
        for job in jobs_list
        if job['min_salary'].isdigit()
    ])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job['min_salary']) > int(job['max_salary']):
            raise ValueError
        return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])
    except (KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_job = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_job.append(job)
        except ValueError:
            pass
    return filter_job
