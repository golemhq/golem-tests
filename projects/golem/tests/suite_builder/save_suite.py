
description = 'Verify the user can make changes to a suite and save it successfully'

pages = ['common',
         'index',
         'suites',
         'suite_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Suites')
    suites.create_access_random_suite()

def test(data):
    clear(suite_builder.workers_input)
    send_keys(suite_builder.workers_input, 3)
    wait(1)
    suite_builder.save_suite()
    refresh_page()
    suite_builder.verify_workers_value(3)
