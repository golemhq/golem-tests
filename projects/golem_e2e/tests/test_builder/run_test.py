
description = 'Verify the user can run a test'

pages = ['common',
         'index',
         'tests',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_' + random('dddd'))
    tests.create_access_test(data.test_name)

def test(data):
    click(test_builder.run_button)
    test_builder.wait_for_test_to_run()
    test_builder.verify_empty_test_execution_modal_content(data.test_name)

