
description = 'Verify the user can run a test from the config modal'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_code',
         'test_run_config_modal',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_run_test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()
    click(test_builder.code_button)

def test(data):
    click(test_builder_code.run_config_button)
    wait_for_element_displayed(test_run_config_modal.config_modal)
    click(test_run_config_modal.run_button)
    test_run_modal.assert_result('success')
