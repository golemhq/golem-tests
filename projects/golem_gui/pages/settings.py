from projects.golem_gui.pages import code_editor


title = ('id', 'settingsTitle', 'page title')
project_editor_container = ('id', 'settingsContainer', 'Project Settings Editor Container')
global_editor_container = ('id', 'globalSettingsContainer', 'Global Settings Editor Container')
save_button = ('id', 'save', 'Save button')


def set_project_value(value):
    code_editor.set_value(value, code_editor_var='projectSettingsEditor')


def assert_project_value(value):
    code_editor.assert_value(value, code_editor_var='projectSettingsEditor')
