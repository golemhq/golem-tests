
description = 'Verify browsers can be selected'

pages = ['common',
         'index',
         'settings',
         'suite_list',
         'suite_builder']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_builder')
    common.navigate_menu('Settings')
    settings.set_project_value('{"remote_browsers": {"browser001": {}}}')
    click(settings.save_button)
    common.navigate_menu('Suites')
    suite_list.create_access_random_suite()


def test(data):
    wait(2)
    press_key(suite_builder.browsers_input, 'SPACE')
    suite_builder.assert_browser_suggestions(['chrome', 'chrome-remote', 'chrome-headless',
                                              'chrome-remote-headless', 'edge', 'edge-remote',
                                              'firefox', 'firefox-headless', 'firefox-remote',
                                              'firefox-remote-headless', 'ie', 'ie-remote',
                                              'opera', 'opera-remote', 'browser001'])
