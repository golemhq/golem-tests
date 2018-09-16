from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify send_keys action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.send_keys('#input-one', 'some text')
    golem_steps.assert_last_step_message("Write 'some text' in element #input-one")
    actions.assert_element_text('#input-one-input-result', 'Welcome some text')
