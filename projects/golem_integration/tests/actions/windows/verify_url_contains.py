from golem import actions


description = 'verify_url_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_url_contains('elements')
    try:
        actions.verify_url_contains('incorrect-partial-url')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "expected URL to contain 'incorrect-partial-url'" in e.args[0]
