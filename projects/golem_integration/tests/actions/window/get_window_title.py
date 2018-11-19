from golem import actions


description = 'Verify get_window_title action'

def test(data):
    actions.navigate(data.env.url)
    assert actions.get_window_title() == 'Web Playground'
    actions.navigate(data.env.url+'elements/')
    assert actions.get_window_title() == 'Web Playground - Elements'