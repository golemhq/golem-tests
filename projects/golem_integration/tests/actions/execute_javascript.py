from golem import actions

description = 'Verify execute_javascript action'

def test(data):
    actions.navigate(data.env.url)
    result = actions.execute_javascript('return arguments[0] + arguments[1]', 'a', 'b')
    assert result == 'ab'