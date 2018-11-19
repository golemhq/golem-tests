from golem import actions


description = 'Verify webdriver.get_window_titles method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    window_titles = actions.get_browser().get_window_titles()
    assert window_titles == ['Web Playground - Tabs', 'Tab']