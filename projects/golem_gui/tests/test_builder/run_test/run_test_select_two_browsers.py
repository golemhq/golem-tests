
description = 'The user can select two browsers before running a test'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_run_config_modal',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_no_envs')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    assert_element_attribute(test_run_config_modal.browser_input, 'value', 'chrome, ')
    clear_element(test_run_config_modal.browser_input)
    test_run_config_modal.select_browser('chrome')
    test_run_config_modal.select_browser('firefox')
    assert_element_attribute(test_run_config_modal.browser_input, 'value', 'chrome, firefox, ')
    click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
