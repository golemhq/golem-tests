from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify submit_prompt_alert action'

def test(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.submit_prompt_alert('hey, some text')
    golem_steps.assert_last_step_message("Submit alert with text 'hey, some text'")
    actions.verify_text_in_element('#result', 'hey, some text')
