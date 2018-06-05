from golem import actions


description = 'Verify javascript_click action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.javascript_click(('id', 'button-one'))
    actions.verify_text_in_element(('id', 'button-one-result'), 'Clicked!')
