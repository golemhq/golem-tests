from golem import actions


description = 'verify_title action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title('Elements')
    try:
        actions.verify_title('incorrect title')
    except Exception as e:
        assert "expected title to be 'incorrect title' but was 'Elements'" in e.args[0]
