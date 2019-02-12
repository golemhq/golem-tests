import time

from selenium.common.exceptions import WebDriverException

from golem.browser import get_browser
from golem import actions


def set_value(code, code_editor_var='codeEditor'):
    script = '{}.setValue(arguments[0])'.format(code_editor_var)
    get_browser().execute_script(script, code)


def get_value(code_editor_var='codeEditor', timeout=5):
    """Use the Javascript codeMirror object to retrieve
    the value of the code editor.
    """
    for _ in range(timeout):
        # Wait until the codeMirror object is initialized
        script = 'return typeof({}) === "undefined"'.format(code_editor_var)
        is_undefined = get_browser().execute_script(script)
        if is_undefined:
            time.sleep(1)
        else:
            break
    script = 'return {}.getValue()'.format(code_editor_var)
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


def assert_value(expected_value, code_editor_var='codeEditor'):
    actions.step('Verify code editor value is: {}'.format(expected_value))
    actual_value = get_value(code_editor_var)
    msg = 'Expected "{}" and received "{}"'.format(expected_value, actual_value)
    assert actual_value == expected_value, msg


def assert_line_value(index, expected_value):
    actions.step('Verify code editor line {} is: {}'.format(index, expected_value))
    value = get_line_value(index)
    msg = 'Expected "{}" and received "{}"'.format(expected_value, value)
    assert value == expected_value, msg