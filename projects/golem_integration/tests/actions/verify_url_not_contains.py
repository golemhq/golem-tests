from golem import actions


description = 'verify_url_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_url_not_contains('incorrect')
    try:
        actions.verify_url_not_contains('elem')
    except Exception as e:
        assert "URL contains 'elem'" in e.args[0]
