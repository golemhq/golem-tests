from golem import actions


description = 'Verify send_keys action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.send_keys('#input-one', 'some text')
    actions.verify_text_in_element('#input-one-input-result', 'Welcome some text')
