from golem import actions


description = 'verify_title_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title_is_not('incorrect title')
    try:
        actions.verify_title_is_not('Elements')
    except Exception as e:
        assert "expected title to not be 'Elements'" in e.args[0]
