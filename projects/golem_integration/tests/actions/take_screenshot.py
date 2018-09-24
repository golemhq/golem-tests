import os

from golem import actions
from golem import execution

from projects.golem_integration.pages import golem_steps


description = 'Verify take_screenshot action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.take_screenshot('my_screenshot')
    golem_steps.assert_last_step_message('my_screenshot')
    listdir = os.listdir(execution.report_directory)
    assert any(x.endswith('.png') for x in listdir)