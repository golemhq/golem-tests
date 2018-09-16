from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify send_text_to_alert action'

def test(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.send_text_to_alert('hey, some text')
    golem_steps.assert_last_step_message("Send 'some text' to alert")
    actions.accept_alert()
    actions.verify_text_in_element('#result', 'hey, some text')
