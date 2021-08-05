import os

from golem import actions
from golem import execution
from projects.golem_integration.pages import golem_logger
from projects.golem_integration.pages import golem_steps


description = 'Verify take_screenshot action'


def test_take_screenshot(data):
    actions.navigate(data.env.url + 'elements/')
    actions.take_screenshot('my_screenshot')
    golem_steps.assert_last_step_message('my_screenshot')
    listdir = os.listdir(execution.test_reportdir)
    assert any(x.endswith('.png') for x in listdir)


def test_take_screenshot_with_alert_present(data):
    actions.navigate(data.env.url + 'alert/')
    actions.click('#alert-button')
    assert actions.get_browser().alert_is_present()
    actions.take_screenshot('my_screenshot_with_alert')
    # screenshot step is not added when an exception is thrown taking
    # the screenshot
    golem_steps.assert_last_step_message('Click #alert-button')
    # screenshot file was not generated
    listdir = os.listdir(execution.test_reportdir)
    assert not any(x.endswith('.png') for x in listdir)
    # The exception was logged
    assert 'There was an error while taking screenshot' in golem_logger.get_info_log()
    assert 'selenium.common.exceptions.UnexpectedAlertPresentException' in golem_logger.get_info_log()
