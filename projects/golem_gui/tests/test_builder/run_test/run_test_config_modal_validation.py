
description = 'The config modal validates: envs exist, processes is a positive integer'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_run_config_modal',
         'test_run_modal']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('run_test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()


def test(data):
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    assert_element_value(test_run_config_modal.processes_input, '1')
    clear_element(test_run_config_modal.processes_input)
    send_keys(test_run_config_modal.processes_input, '0')
    click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Processes must be at least one')
    refresh_page()
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    clear_element(test_run_config_modal.processes_input)
    send_keys(test_run_config_modal.processes_input, 'abc')
    click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Processes must be an integer')
    refresh_page()
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    send_keys(test_run_config_modal.environments_input, 'not-existent-env')
    click(test_run_config_modal.run_button)
    common.assert_info_bar_message('Environment not-existent-env does not exist for project run_test')
