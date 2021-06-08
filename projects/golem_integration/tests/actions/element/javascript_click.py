from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify javascript_click action'


def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.javascript_click(('id', 'button-one'))
    golem_steps.assert_last_step_message('Javascript click element button-one')
    actions.verify_element_text(('id', 'button-one-result'), 'Clicked!')
