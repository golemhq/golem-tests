
description = 'Verify the user can delete a test'

pages = ['common',
         'index',
         'test_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_list')
    store('test_name', 'test' + random('ddddd'))
    test_list.add_test(data.test_name)


def test(data):
    test_list.click_delete_button(data.test_name)
    common.confirm_confirm_modal()
    common.assert_toast_message_is_displayed('File {} was removed'.format(data.test_name))
    assert not test_list.test_exists(data.test_name)
    refresh_page()
    assert not test_list.test_exists(data.test_name)
