from golem.browser import get_browser, element
from golem import actions


def set_value(code, code_mirror_selector='div.CodeMirror'):
    """Set the value of the CodeMirror editor found by the selector"""
    code_mirror = element(code_mirror_selector)
    script = 'arguments[0].CodeMirror.setValue(arguments[1])'
    get_browser().execute_script(script, code_mirror, code)


def get_value(code_mirror_selector='div.CodeMirror', timeout=5):
    """Use the Javascript codeMirror object to retrieve
    the value of the code editor.
    """
    get_browser().wait_for_element_present('div.CodeMirror', timeout)
    code_mirror = element(code_mirror_selector)
    script = 'return arguments[0].CodeMirror.getValue()'
    all_code = get_browser().execute_script(script, code_mirror)
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


def assert_value(expected_value, code_mirror_selector='div.CodeMirror'):
    actions.step('Verify code editor value is: {}'.format(expected_value))
    actual_value = get_value(code_mirror_selector)
    msg = 'Expected "{}" and received "{}"'.format(expected_value, actual_value)
    assert actual_value == expected_value, msg


def assert_line_value(index, expected_value):
    actions.step('Verify code editor line {} is: {}'.format(index, expected_value))
    value = get_line_value(index)
    msg = 'Expected "{}" and received "{}"'.format(expected_value, value)
    assert value == expected_value, msg