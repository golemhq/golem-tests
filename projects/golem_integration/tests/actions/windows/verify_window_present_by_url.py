from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_window_present_by_url action'

def test(data):
    tabs_url = data.env.url+'tabs/'
    elements_url = data.env.url + 'elements/'
    actions.navigate(tabs_url)
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.verify_window_present_by_url(tabs_url)
    golem_steps.assert_last_step_message("Verify window present by URL '{}'".format(tabs_url))
    actions.verify_window_present_by_url(elements_url)
