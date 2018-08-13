from golem import actions


description = 'Verify get_window_titles action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    window_titles = actions.get_window_titles()
    assert window_titles == ['Tabs', 'Tab']