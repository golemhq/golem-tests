from golem import actions


description = 'verify_title_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_title_not_contains('incorrect title')
    try:
        actions.verify_title_not_contains('Elem')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "title contains 'Elem'" in e.args[0]
