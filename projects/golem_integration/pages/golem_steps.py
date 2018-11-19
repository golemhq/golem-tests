from golem import execution, actions


def get_last_step_message():
    return execution.steps[-1]['message']


def get_last_error():
    return execution.errors[-1]


def assert_last_step_message(expected):
    error = "Expected '{}' but got '{}'".format(expected, get_last_step_message())
    assert get_last_step_message() == expected, error


def assert_last_error(message, description=''):
    actions.step("Assert last error is '{}'".format(message))
    last_error = get_last_error()
    error = "expected '{}', got '{}'".format(message, last_error['message'])
    assert last_error['message'] == message, error
    error = "expected '{}', got '{}'".format(description, last_error['description'])
    assert last_error['description'] == description, error
    # remove error from last step
    execution.steps.pop()
    # remove error from execution.errors
    execution.errors.pop()
