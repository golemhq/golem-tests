from golem import actions


description = 'Verify webdriver.get_window_index method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    assert actions.get_browser().get_window_index() == 0
    actions.switch_to_window_by_index(1)
    assert actions.get_browser().get_window_index() == 1
