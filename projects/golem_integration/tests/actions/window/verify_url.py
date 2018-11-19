from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_url action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.verify_url(url)
    golem_steps.assert_last_step_message("Verify URL is '{}'".format(url))
    actions.verify_url('http://incorrect_url')
    exp = "expected URL to be 'http://incorrect_url' but was '{}'".format(url)
    golem_steps.assert_last_error(exp)
