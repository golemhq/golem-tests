from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_enabled action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_enabled('#input-one')
    golem_steps.assert_last_step_message('Assert element #input-one is enabled')
    actions.navigate(data.env.url+'disabled-elements/')
    try:
        actions.assert_element_enabled('#text')
    except AssertionError as e:
        assert 'element #text is not enabled' in e.args[0]
