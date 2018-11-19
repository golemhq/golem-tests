from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify submit_form action'

def test(data):
    actions.navigate(data.env.url + 'form-basic/')
    actions.send_keys('#name', 'foo')
    actions.submit_form('#form1')
    golem_steps.assert_last_step_message('Submit form')
    actions.assert_element_text('label#name', 'foo')
