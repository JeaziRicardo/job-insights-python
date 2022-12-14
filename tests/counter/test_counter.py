from pytest import raises
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "jobs") == 306

    assert count_ocurrences("data/jobs.csv", "jOBs") == 306

    assert count_ocurrences("data/jobs.csv", "xablau") == 0

    assert count_ocurrences("data/jobs.csv", "XablaU") == 0

    with raises(TypeError):
        count_ocurrences()

    with raises(AttributeError):
        count_ocurrences("data/jobs.csv", 28)

    with raises(FileNotFoundError):
        count_ocurrences("dat/jobs.csv", "jobs")
