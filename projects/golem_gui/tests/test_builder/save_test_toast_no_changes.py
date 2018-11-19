
description = 'Verify the application displays a toast message when saving a test when there are no unsaved changes'

pages = ['common',
         'index',
         'test_list',
         'test_builder']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    common.navigate_menu('Tests')
    store('test_name', 'test_' + random('dddd'))
    test_list.create_access_test(data.test_name)

def test(data):
    test_builder.add_action('click')
    test_builder.save_test()
    refresh_page()
    click(test_builder.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test_name+' saved')
