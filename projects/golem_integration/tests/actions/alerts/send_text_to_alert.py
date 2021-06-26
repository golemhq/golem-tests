from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify send_text_to_alert action'


def test_send_text_to_alert(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.send_text_to_alert('hey, some text')
    golem_steps.assert_last_step_message("Send 'hey, some text' to alert")
    actions.accept_alert()
    actions.verify_element_text('#result', 'hey, some text')
