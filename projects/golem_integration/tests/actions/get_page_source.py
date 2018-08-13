from golem import actions


description = 'Verify get_page_source action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    assert '<button id="button-one"' in actions.get_page_source()
