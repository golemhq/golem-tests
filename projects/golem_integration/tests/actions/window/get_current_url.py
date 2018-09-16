from golem import actions


description = 'Verify get_current_url action'

def test(data):
    actions.navigate(data.env.url)
    assert actions.get_current_url() == data.env.url
