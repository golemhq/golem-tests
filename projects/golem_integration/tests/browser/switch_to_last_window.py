from golem import actions


description = 'Verify webdriver.switch_to_last_window method'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#title', 'SECOND TAB')
    actions.click('#goButtonCustom')
    actions.clear_element('#title')
    actions.send_keys('#title', 'THIRD TAB')
    actions.click('#goButtonCustom')
    actions.wait_for_window_present_by_title('SECOND TAB', timeout=10)
    actions.wait_for_window_present_by_title('THIRD TAB', timeout=10)
    actions.get_browser().switch_to_window_by_index(2)
    assert actions.get_window_index() == 2
    actions.navigate(data.env.url)
    actions.switch_to_first_window()
    actions.verify_title('Tabs')
    actions.get_browser().switch_to_last_window()
    assert actions.get_window_index() == 2
    actions.verify_title('Index')