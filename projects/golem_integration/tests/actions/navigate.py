from golem import actions


description = 'Verify navigate action'

def test(data):
    actions.navigate(data.env.url)
    assert actions.get_browser().current_url == data.env.url
