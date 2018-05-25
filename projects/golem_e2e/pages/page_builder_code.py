from golem import actions
from golem.browser import elements, element, get_browser


save_button = ('id', 'save', 'Save button')
preview_button = ('id', 'loadGuiButton', 'Preview button')


def write_code(code):
    # first_line = element('.CodeMirror-code .CodeMirror-line')
    # first_line.send_keys(code)\
    script = 'codeEditor.setValue(arguments[0])'
    get_browser().execute_script(script, code)


def verify_page_code(code):
    # actual_code = element('div.CodeMirror-code').text
    script = 'return codeEditor.getValue()'
    actual_code = get_browser().execute_script(script)
    assert actual_code == code
