
description = 'Verify an error is shown when duplicating a test with existing name'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    common.navigate_menu('Tests')
    store('test_name', 'test' + random('dddd'))
    store('test_name2', 'test' + random('dddd'))
    test_list.add_test(data.test_name)
    test_list.add_test(data.test_name2)


def test(data):
    test_list.rename_test(data.test_name, data.test_name2)
    common.assert_error_message('A file with that name already exists')
