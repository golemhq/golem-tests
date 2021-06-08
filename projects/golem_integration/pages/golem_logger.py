import os

from golem import execution


def get_last_info_log_line():
    test_file_reportdir = os.path.dirname(execution.report_directory)  # TODO
    path = os.path.join(test_file_reportdir, 'execution_info.log')
    with open(path) as f:
        return f.readlines()[-1]


def last_info_log_line_contains(partial):
    return partial in get_last_info_log_line()
