from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can edit the test name by clicking on the title'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    data.test = api.test.create_access_test(data.project)


def test(data):
    actions.click(test_builder.test_name)
    actions.assert_element_displayed(test_builder.test_name_input)
    actions.assert_element_value(test_builder.test_name_input, data.test)
    actions.send_keys(test_builder.test_name_input, 'new')
    actions.press_key(test_builder.test_name_input, 'TAB')
    common.assert_toast_message_is_displayed('File was renamed')
    new_name = data.test + 'new'
    actions.wait_for_element_displayed(test_builder.test_name, 5)
    actions.assert_element_text(test_builder.test_name, new_name)
    actions.refresh_page()
    actions.assert_element_text(test_builder.test_name, new_name)
