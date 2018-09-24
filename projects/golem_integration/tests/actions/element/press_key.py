from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify press_key action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.press_key(('id', 'input-one'), 'NUMPAD2')
    golem_steps.assert_last_step_message("Press key: 'NUMPAD2' in element input-one")
    actions.assert_element_text(('id', 'input-one-input-result'), 'Welcome 2')
    try:
        actions.press_key(('id', 'input-one'), 'UNDEFINED_KEY')
    except Exception as e:
        assert 'Key UNDEFINED_KEY is invalid' in e.args[0]
    else:
        raise AssertionError('expected an exception')