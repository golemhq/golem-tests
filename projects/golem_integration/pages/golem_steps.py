from golem import execution


def get_last_step_message():
    return execution.steps[-1]['message']


def get_last_error():
    return execution.errors[-1]


def assert_last_step_message(expected):
    assert get_last_step_message() == expected


def assert_last_error(message, description=''):
    assert get_last_error()['message'] == message
    assert get_last_error()['description'] == description
    # remove error from last step
    execution.steps[-1] = None
    # remove error from execution.errors
    execution.errors.pop()
