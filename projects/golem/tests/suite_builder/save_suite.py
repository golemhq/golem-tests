
description = 'Verify the user can make changes to a suite and save it successfully'

pages = ['login',
         'index',
         'project_suites',
         'suite_builder']

def setup(data):
    navigate(data.env.url)
    login.do_login('admin', 'admin')
    index.create_access_project('test')

def test(data):
    project_suites.create_access_suite('test_save_suite' + random('ddd'))
    clear(suite_builder.workers_input)
    send_keys(suite_builder.workers_input, 3)
    wait(1)
    suite_builder.save_suite()
    refresh_page()
    suite_builder.verify_workers_value(3)


def teardown(data):
    close()
