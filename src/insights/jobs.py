from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        reader = csv.DictReader(file)
        jobs_list = list(reader)
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    types_set = set()
    for job in jobs_list:
        types_set.add(job['job_type'])
    return list(types_set)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]
