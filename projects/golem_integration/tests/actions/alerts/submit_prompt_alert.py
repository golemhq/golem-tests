from golem import actions


description = 'Verify submit_prompt_alert action'

def test(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.submit_prompt_alert('hey, some text')
    actions.verify_text_in_element('#result', 'hey, some text')
