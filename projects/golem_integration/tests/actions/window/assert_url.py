from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_url action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.assert_url(url)
    golem_steps.assert_last_step_message("Assert URL is '{}'".format(url))
    msg = "expected URL to be 'http://incorrect_url' but was '{}'".format(url)
    with expected_exception(AssertionError, msg):
        actions.assert_url('http://incorrect_url')
