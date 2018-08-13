from golem import actions


description = 'Verify webelement.javascript_click method'

def test(data):
    actions.navigate(data.env.url+'elements/')
    element = actions.get_browser().find('#button-one')
    print(type(element))
    element.javascript_click()
    actions.verify_text_in_element(('id', 'button-one-result'), 'Clicked!')
