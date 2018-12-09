
description = 'The user can select two environments, browsers and data sets before running a test'

pages = ['common',
         'environments',
         'index',
         'test_list',
         'test_builder',
         'test_builder_common',
         'test_run_config_modal',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_two_envs')
    common.navigate_menu('Environments')
    environments.set_value('{"foo": {}, "bar": {}}')
    click(environments.save_button)
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    test_builder_common.add_variable_to_datatable('foo', ['1', '2'])
    test_builder.save_test()
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    clear_element(test_run_config_modal.browser_input)
    test_run_config_modal.select_browser('chrome')
    test_run_config_modal.select_browser('firefox')
    test_run_config_modal.select_env('foo')
    test_run_config_modal.select_env('bar')
    click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(8)
