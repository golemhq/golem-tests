
description = 'Verify the user can delete a page'

pages = ['common',
         'index',
         'page_list']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('page_list')
    store('page_name', 'page' + random('dddd'))
    common.navigate_menu('Pages')
    page_list.add_page(data.page_name)


def test(data):
    page_list.click_delete_button(data.page_name)
    common.confirm_confirm_modal()
    common.assert_toast_message_is_displayed('File {} was removed'.format(data.page_name))
    assert not page_list.page_exists(data.page_name)
    refresh_page()
    assert not page_list.page_exists(data.page_name)
