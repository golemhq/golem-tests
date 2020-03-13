from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import settings
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import suite_builder


description = 'Verify browsers can be selected'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('suite_builder')
    common.navigate_menu('Project Settings')
    settings.set_settings_value('{"remote_browsers": {"browser001": {}}}')
    actions.click(settings.save_button)
    api.suite.create_access_random_suite('suite_builder')


def test(data):
    actions.wait(2)
    actions.press_key(suite_builder.browsers_input, 'SPACE')
    suite_builder.assert_browser_suggestions(['chrome', 'chrome-remote', 'chrome-headless',
                                              'chrome-remote-headless', 'edge', 'edge-remote',
                                              'firefox', 'firefox-headless', 'firefox-remote',
                                              'firefox-remote-headless', 'ie', 'ie-remote',
                                              'opera', 'opera-remote', 'browser001'])
