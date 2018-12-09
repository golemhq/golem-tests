
description = 'The user can add two data sets before running a test'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_common',
         'test_run_config_modal',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('project_no_envs')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    test_builder_common.add_variable_to_datatable('foo', ['1', '2'])
    click(test_builder.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_amount_of_sets(2)
