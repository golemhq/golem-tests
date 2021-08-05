from golem import actions


description = 'Verify webelement.press_key method'


def test_press_key(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#input-one')
    element.press_key('NUMPAD2')
    actions.wait(0.5)
    actions.verify_element_text('#input-one-input-result', 'Welcome 2')


def test_press_invalid_key(data):
    actions.navigate(data.env.url + 'elements/')
    try:
        element = actions.get_browser().find('#input-one')
        element.press_key('UNDEFINED_KEY')
    except Exception as e:
        assert 'Key UNDEFINED_KEY is invalid' in e.args[0]
    else:
        raise AssertionError('expected an exception')
