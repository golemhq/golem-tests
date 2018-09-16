from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify execute_javascript action'

def test(data):
    actions.navigate(data.env.url)
    script = 'return arguments[0] + arguments[1]'
    args = ('a', 'b')
    result = actions.execute_javascript(script, 'a', 'b')
    expected = "Execute javascript code '{}' with args '{}'".format(script, args)
    golem_steps.assert_last_step_message(expected)
    assert result == 'ab'
