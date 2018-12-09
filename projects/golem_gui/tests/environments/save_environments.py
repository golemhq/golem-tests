
description = 'Verify project environments can be modified and saved'

pages = ['common',
         'index',
         'environments']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test_environments')

def test(data):
    store('code', '{\n"test": {"url": "foo"}\n}')
    common.navigate_menu('Environments')
    environments.set_value(data.code)
    click(environments.save_button)
    common.assert_toast_message_is_displayed('Environments saved')
    refresh_page()
    environments.assert_value(data.code)
