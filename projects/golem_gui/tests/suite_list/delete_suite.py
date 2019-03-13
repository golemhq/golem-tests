
description = 'Verify the user can delete a suite'

pages = ['common',
         'index',
         'suite_list']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    store('suite_name', 'suite_' + random('dddd'))
    suite_list.add_suite(data.suite_name)

def test(data):
    suite_list.click_delete_button(data.suite_name)
    common.confirm_confirm_modal()
    common.assert_toast_message_is_displayed('File {} was removed'.format(data.suite_name))
    assert not suite_list.suite_exists(data.suite_name)
    refresh_page()
    assert not suite_list.suite_exists(data.suite_name)
