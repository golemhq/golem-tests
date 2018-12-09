
description = 'The app will prompt the user to select one env when there is more than one'

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
    click(test_builder.run_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    assert_element_displayed(test_run_config_modal.config_modal)
    # TODO: assert_element_displayed should wait
    common.assert_info_bar_message('Select at least one environment')
