
description = 'Verify the user cannot create a new suite if a suite with the same name exists'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    store('suite_name', 'suite' + random('dddd'))
    suite_list.add_suite(data.suite_name)
    suite_list.add_suite(data.suite_name)
    common.assert_error_message('A suite with that name already exists')
