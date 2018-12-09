from projects.golem_gui.pages import code_editor


save_button = ('id', 'save', 'Save button')


def set_value(value):
    code_editor.set_value(value, code_editor_var='environmentsEditor')


def assert_value(value):
    code_editor.assert_value(value, code_editor_var='environmentsEditor')
