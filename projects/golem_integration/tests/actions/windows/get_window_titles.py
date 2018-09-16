from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'close_window_by_title action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#title', 'foo')
    actions.click('#goButton')
    actions.send_keys('#title', 'bar')
    actions.click('#goButton')
    actions.assert_amount_of_windows(3)
    titles = actions.get_window_titles()
    expected = ['Tabs', 'foo', 'bar']
    assert sorted(titles) == sorted(expected)
