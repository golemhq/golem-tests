from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify go_forward action'

def test(data):
    elements_url = data.env.url + 'elements/'
    actions.navigate(data.env.url)
    actions.click(('link_text', 'Elements'))
    assert actions.get_current_url() == elements_url
    actions.go_back()
    assert actions.get_current_url() == data.env.url
    actions.go_forward()
    golem_steps.assert_last_step_message('Go forward')
    assert actions.get_current_url() == elements_url
