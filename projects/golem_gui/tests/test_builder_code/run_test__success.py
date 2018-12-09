
description = 'Verify the user can run an empty test'

pages = ['common',
         'index',
         'test_list',
         'test_builder',
         'test_builder_code',
         'test_run_modal']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    test_list.create_access_random_test()

def test(data):
    click(test_builder.code_button)
    click(test_builder_code.run_button)
    test_run_modal.wait_for_test_to_run()
    test_run_modal.assert_result('success')
