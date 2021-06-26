from golem import actions


description = 'Verify webelement.javascript_click method'


def test(data):
    actions.navigate(data.env.url+'elements/')
    element = actions.get_browser().find('#button-one')
    element.javascript_click()
    actions.verify_element_text(('id', 'button-one-result'), 'Clicked!')
