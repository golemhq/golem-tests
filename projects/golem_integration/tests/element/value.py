from golem import actions


description = 'Verify webelement.value property'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#input-one')
    assert element.value == ''
    element.send_keys('some value')
    assert element.value == 'some value'

