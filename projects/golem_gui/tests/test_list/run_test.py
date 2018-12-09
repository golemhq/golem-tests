
description = 'Verify the user can run an empty test'

pages = ['common',
         'index',
         'test_list',
         'test_run_modal',
         'test_run_config_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_no_envs')
    common.navigate_menu('Tests')
    store('test_name', 'test'+random('ddddd'))
    test_list.add_test(data.test_name)

def test(data):
    test_list.click_run_test(data.test_name)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    click(test_run_config_modal.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result('success')
