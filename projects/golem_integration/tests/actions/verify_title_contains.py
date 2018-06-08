from golem import actions


description = 'verify_title_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title_contains('Elem')
    try:
        actions.verify_title_contains('incorrect title')
    except Exception as e:
        assert "expected title to contain 'incorrect title'" in e.args[0]
