from typing import List, Dict
from src.insights.jobs import (read)


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    industries_set = set()
    for job in jobs_list:
        if job['industry'] != '':
            industries_set.add(job['industry'])
    return list(industries_set)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job['industry'] == industry]
