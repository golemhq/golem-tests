from golem import actions


description = 'verify_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_page_contains_text('Special Elements')
    try:
        actions.verify_page_contains_text('THIS TEXT IS NOT PRESENT')
    except Exception as e:
        assert "Text 'THIS TEXT IS NOT PRESENT' not found in page" in e.args[0]
