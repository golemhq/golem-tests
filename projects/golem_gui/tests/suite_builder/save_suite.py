
description = 'Verify the user can make changes to a suite and save it successfully'

tags = ['smoke']

pages = ['common',
         'index',
         'suite_builder',
         'suite_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')
    suite_list.create_access_random_suite()

def test(data):
    clear_element(suite_builder.processes_input)
    send_keys(suite_builder.processes_input, 3)
    suite_builder.save_suite()
    refresh_page()
    suite_builder.assert_processes_value(3)

def teardown(data):
    pass
