from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_url_is_not action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.verify_url_is_not('http://incorrect')
    golem_steps.assert_last_step_message("Verify URL is not 'http://incorrect'")
    actions.verify_url_is_not(url)
    golem_steps.assert_last_error("expected URL to not be '{}'".format(url))
