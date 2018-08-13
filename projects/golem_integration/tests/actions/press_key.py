from golem import actions

description = 'Verify press_key action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.press_key(('id', 'input-one'), 'NUMPAD2')
    actions.verify_text_in_element(('id', 'input-one-input-result'), 'Welcome 2')
    try:
        actions.press_key(('id', 'input-one'), 'UNDEFINED_KEY')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Key UNDEFINED_KEY is invalid' in e.args[0]
