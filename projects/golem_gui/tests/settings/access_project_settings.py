
description = 'Verify settings page contains settings for project and global'

pages = ['common',
         'index',
         'settings']

def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')

def test(data):
    common.navigate_menu('Settings')
    assert_element_text(settings.title, 'Test - Settings')
    assert_element_displayed(settings.project_editor_container)
    assert_element_displayed(settings.global_editor_container)