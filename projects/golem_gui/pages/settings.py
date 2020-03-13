from projects.golem_gui.pages import code_editor


title = ('id', 'settingsTitle', 'page title')
settings_editor = ('id', 'settingsContainer', 'Settings Editor Container')
save_button = ('id', 'save', 'Save button')


def set_settings_value(value):
    code_editor.set_value(value)


def assert_settings_value(value):
    code_editor.assert_value(value)
