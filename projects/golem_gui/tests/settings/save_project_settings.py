
description = 'Verify project settings can be modified and saved'

tags = ['smoke']

pages = ['common',
         'index',
         'settings']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_project_settings')

def test(data):
    common.navigate_menu('Settings')
    settings.set_project_value('{\n"search_timeout": 10\n}')
    click(settings.save_button)
    common.assert_toast_message_is_displayed('Settings saved')
    refresh_page()
    settings.assert_project_value('{\n"search_timeout": 10\n}')

def teardown(data):
    pass
