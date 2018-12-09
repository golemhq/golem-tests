
description = 'Verify settings page contains global settings only'

pages = ['common',
         'index',
         'settings']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)

def test(data):
    common.navigate_menu('Settings')
    assert_element_text(settings.title, 'Settings')
    assert_element_not_displayed(settings.project_editor_container)
    assert_element_displayed(settings.global_editor_container)