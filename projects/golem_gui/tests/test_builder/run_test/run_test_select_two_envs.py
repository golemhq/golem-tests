
description = 'The user can select two environments before running a test'

pages = ['common',
         'environments',
         'index',
         'test_list',
         'test_builder',
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
    click(test_builder.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    test_run_config_modal.select_env('foo')
    test_run_config_modal.select_env('bar')
    assert_element_attribute(test_run_config_modal.environments_input, 'value', 'foo, bar, ')
    click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
