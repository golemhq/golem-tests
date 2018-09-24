from golem import actions

description = 'Verify activate_browser throws error when browser_id is incorrect'


def test(data):
    actions.open_browser()
    actions.navigate(data.env.url)
    try:
        actions.activate_browser('second_browser')
    except Exception as e:
        assert 'is not a valid browser id' in e.args[0]
