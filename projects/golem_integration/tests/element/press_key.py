from golem import actions

description = 'Verify webelement.press_key method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#input-one')
    element.press_key('NUMPAD2')
    actions.verify_text_in_element('#input-one-input-result', 'Welcome 2')
    try:
        element = actions.get_browser().find('#input-one')
        element.press_key('UNDEFINED_KEY')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Key UNDEFINED_KEY is invalid' in e.args[0]
