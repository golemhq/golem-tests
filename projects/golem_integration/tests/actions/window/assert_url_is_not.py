from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_url_is_not action'

def test(data):
    url = data.env.url+'elements/'
    actions.navigate(url)
    actions.assert_url_is_not('http://incorrect')
    golem_steps.assert_last_step_message("Assert URL is not 'http://incorrect'")
    try:
        actions.assert_url_is_not(url)
    except AssertionError as e:
        assert "expected URL to not be '{}'".format(url) in e.args[0]
