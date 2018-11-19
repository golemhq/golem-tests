from golem import actions


description = 'Verify get action'

def test(data):
    actions.get(data.env.url)
    assert actions.get_browser().current_url == data.env.url
