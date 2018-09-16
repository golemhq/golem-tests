import os

from golem import execution


def get_last_info_log_line():
    path = os.path.join(execution.report_directory, 'execution_info.log')
    with open(path) as f:
        return f.readlines()[-1]


def last_info_log_line_contains(partial):
    return partial in get_last_info_log_line()
