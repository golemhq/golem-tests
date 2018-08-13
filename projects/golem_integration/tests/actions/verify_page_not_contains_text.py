from golem import actions


description = 'verify_page_not_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_page_not_contains_text('THIS TEXT IS NOT PRESENT')
    try:
        actions.verify_page_not_contains_text('Special Elements')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "text 'Special Elements' was found in page" in e.args[0]
