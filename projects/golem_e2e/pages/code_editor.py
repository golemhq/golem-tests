from golem.browser import get_browser
from golem import actions


def set_value(code):
    script = 'codeEditor.setValue(arguments[0])'
    get_browser().execute_script(script, code)


def get_value():
    script = 'return codeEditor.getValue()'
    all_code = get_browser().execute_script(script)
    return all_code


def get_line_value(index):
    script = 'return codeEditor.getLine(arguments[0])'
    return get_browser().execute_script(script, index)


def set_line_value(index, value):
    script = ('var lineLength = codeEditor.getLine(arguments[0]).length;'
              'var from = {line: arguments[0], ch: 0};'
              'var to = {line: arguments[0], ch: lineLength};'
              'codeEditor.replaceRange(arguments[1], from, to);')
    get_browser().execute_script(script, index, value)


def assert_value(expected_value):
    actions.step('Verify code editor value is: {}'.format(expected_value))
    actual_value = get_value()
    msg = 'Expected "{}" and received "{}"'.format(expected_value, actual_value)
    assert actual_value == expected_value, msg


def assert_line_value(index, expected_value):
    actions.step('Verify code editor line {} is: {}'.format(index, expected_value))
    value = get_line_value(index)
    msg = 'Expected "{}" and received "{}"'.format(expected_value, value)
    assert value == expected_value, msg