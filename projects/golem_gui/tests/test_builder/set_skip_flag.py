from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the skip flag can be set to True and to a str'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test(data):
    actions.assert_element_not_checked(test_builder.skip_checkbox)
    actions.assert_element_not_displayed(test_builder.skip_message_input)
    actions.check_element(test_builder.skip_checkbox)
    actions.assert_element_displayed(test_builder.skip_message_input)
    actions.assert_element_value(test_builder.skip_message_input, '')
    test_builder.save_test()
    actions.refresh_page()
    actions.assert_element_checked(test_builder.skip_checkbox)
    actions.assert_element_displayed(test_builder.skip_message_input)
    actions.assert_element_value(test_builder.skip_message_input, '')
    actions.send_keys(test_builder.skip_message_input, 'skip message')
    test_builder.save_test()
    actions.refresh_page()
    actions.assert_element_checked(test_builder.skip_checkbox)
    actions.assert_element_displayed(test_builder.skip_message_input)
    actions.assert_element_value(test_builder.skip_message_input, 'skip message')
    actions.uncheck_element(test_builder.skip_checkbox)
    test_builder.save_test()
    actions.assert_element_not_checked(test_builder.skip_checkbox)
    actions.assert_element_not_displayed(test_builder.skip_message_input)
