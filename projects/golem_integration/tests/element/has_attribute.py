from golem import actions


description = 'Verify webelement.has_attribute method'

def test(data):
    actions.navigate(data.env.url+'elements/')
    button = actions.get_browser().find('#button-one')
    assert button.has_attribute('onclick')
    assert not button.has_attribute('not-this-one')

