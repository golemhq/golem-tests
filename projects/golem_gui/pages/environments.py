from projects.golem_gui.pages import code_editor, common

from golem.browser import element


save_button = ('id', 'save', 'Save button')


def save():
    element(save_button).click()
    common.assert_toast_message_is_displayed('Environments saved')


def set_value(value):
    code_editor.set_value(value)


def get_value():
    return code_editor.get_value()
