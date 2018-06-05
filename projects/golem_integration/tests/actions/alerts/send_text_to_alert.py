from golem import actions


description = 'Verify send_text_to_alert action'

def test(data):
    actions.navigate(data.env.url + 'prompt/')
    actions.click('#prompt-button')
    actions.send_text_to_alert('hey, some text')
    actions.accept_alert()
    actions.verify_text_in_element('#result', 'hey, some text')
