from golem import actions


description = 'get_window_titles action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#title', 'foo')
    actions.click('#goButtonCustom')
    actions.clear_element('#title')
    actions.send_keys('#title', 'bar')
    actions.click('#goButtonCustom')
    actions.assert_amount_of_windows(3)
    titles = actions.get_window_titles()
    expected = ['Tabs', 'foo', 'bar']
    assert sorted(titles) == sorted(expected)
