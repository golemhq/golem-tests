
description = 'Verify the user can create a suite with a name that contains spaces in the middle and they are replaces with underscores'

pages = ['common',
         'index',
         'suite_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_list')


def test(data):
    store('suite_name', 'suite' + random('dddd'))
    suite_list.add_suite(data.suite_name + ' with spaces')
    suite_list.assert_suite_exists(data.suite_name + '_with_spaces')
