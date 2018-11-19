import os

from golem import actions
from golem import execution


description = 'Verify _capture_screenshot'

def test(data):
    actions.navigate(data.env.url)
    actions._capture_screenshot('my_screenshot.png')
    path = os.path.join(execution.report_directory, 'my_screenshot.png')
    assert os.path.isfile(path)
