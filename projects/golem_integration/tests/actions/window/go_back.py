from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify go_back action'

def test(data):
    actions.navigate(data.env.url)
    actions.click(('link_text', 'Elements'))
    assert actions.get_current_url() == data.env.url + 'elements/'
    actions.go_back()
    golem_steps.assert_last_step_message('Go back')
    assert actions.get_current_url() == data.env.url
